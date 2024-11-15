
###################################################################################
# Imports
###################################################################################
import numpy as np
import matplotlib.pyplot as plt

###################################################################################
# Functions
###################################################################################
# Sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x)) - (1/2)
    # return np.tanh(x)     # for replacement with Tanh function

# Nearest POT function
def nearest_power_of_two(x):
    return 2 ** np.round(np.log2(x))

###################################################################################
# Constants
###################################################################################
x_interval = 8  # Input interval = [-x_interval, +x_interval]
bw_segment = 2  # Number of segments = 2**bw_segment
bw_total   = 16 # Bit width of the input/output

# Constants
x_cont_points   = 2**bw_total
x_seg_points    = 2**bw_segment

###################################################################################
# Original and base functions
###################################################################################
# Generate continuous x values
x_continuous = np.linspace(-x_interval, x_interval, 1+x_cont_points)
x_segmented  = np.linspace(-x_interval, x_interval, 1+x_seg_points)

# Compute y values using the sigmoid functions for x_continuous
y_sigmoid   = sigmoid(x_continuous)

# Compute y values using the sigmoid functions for x_segmented
y_sigmoid_s = sigmoid(x_segmented)

# Interpolate y_sigmoid_i preserving straight lines based on x_continuous
y_sigmoid_i = np.interp(x_continuous, x_segmented, sigmoid(x_segmented))

###################################################################################
# Calculate slopes and their POTs
###################################################################################
slopes_sigmoid_s = []

for k in range(len(x_segmented) - 1):
    delta_x_sigmoid = x_segmented[k + 1] - x_segmented[k]
    delta_y_sigmoid = y_sigmoid_s[k + 1] - y_sigmoid_s[k]

    # Avoid division by zero
    if delta_x_sigmoid != 0:
        slope_sigmoid = delta_y_sigmoid / delta_x_sigmoid
        slopes_sigmoid_s.append(slope_sigmoid)
slopes_sigmoid_s.append(slopes_sigmoid_s[-1])    #added for later calculations

slopes_sigmoid_POT = [nearest_power_of_two(slope) for slope in slopes_sigmoid_s]

###################################################################################
# Calculations with respect to alpha_star_n
###################################################################################
y_sigmoid_n = []
alpha_star_n = []
for n in range(len(x_segmented) - 1):
    alpha_diff_sum = 0
    for m in range(len(x_continuous)):
        if (x_continuous[m] >= x_segmented[n] and x_continuous[m] < x_segmented[n+1]):
            line_sigmoid = (slopes_sigmoid_POT[n] * x_continuous[m]) + y_sigmoid_s[n] - (slopes_sigmoid_POT[n] * x_segmented[n])
            y_sigmoid_n.append(line_sigmoid)
            alpha_diff_sum = alpha_diff_sum + (y_sigmoid[m] - line_sigmoid)

    alpha_star_n.append(alpha_diff_sum)

line_sigmoid_last = (slopes_sigmoid_POT[-1] * x_continuous[-1]) + y_sigmoid_s[-1] - (slopes_sigmoid_POT[-1] * x_segmented[-1])
y_sigmoid_n.append(line_sigmoid_last)

alpha_diff_sum_last = alpha_diff_sum + (y_sigmoid[-1] - line_sigmoid_last)
alpha_star_n.append(alpha_diff_sum_last)

# shift y-intercept according to alpha
lat_sigmoid_POT = [y + alpha / 2**(bw_total-bw_segment) for y, alpha in zip(y_sigmoid_s, alpha_star_n)]

# new y_sigmoid_n according to alpha values
y_sigmoid_n = []
for n in range(len(x_segmented) - 1):
    for m in range(len(x_continuous)):
        if (x_continuous[m] >= x_segmented[n] and x_continuous[m] < x_segmented[n+1]):
            line_sigmoid = (slopes_sigmoid_POT[n] * x_continuous[m]) + lat_sigmoid_POT[n] - (slopes_sigmoid_POT[n] * x_segmented[n])
            y_sigmoid_n.append(line_sigmoid)

line_sigmoid_last = (slopes_sigmoid_POT[-1] * x_continuous[-1]) + lat_sigmoid_POT[-1] - (slopes_sigmoid_POT[-1] * x_segmented[-1])
y_sigmoid_n.append(line_sigmoid_last)

y_sigmoid_n_alpha = y_sigmoid_n


###################################################################################
# Calculations with respect to beta_star_n
###################################################################################
# calculate beta values according to (max+min)/2
dif = (y_sigmoid - y_sigmoid_n)
max_dif_seg = []
min_dif_seg = []

for n in range(len(x_segmented) - 1):
    dif_seg = []
    for m in range(len(x_continuous)):
        if (x_continuous[m] >= x_segmented[n] and x_continuous[m] < x_segmented[n+1]):
            dif_seg.append(dif[m])

    max_dif_seg.append(max(dif_seg))
    min_dif_seg.append(min(dif_seg))

beta_seg = [(max_val + min_val) / 2 for max_val, min_val in zip(max_dif_seg, min_dif_seg)]

# new y_sigmoid_n according to beta values
y_sigmoid_n = []
for n in range(len(x_segmented) - 1):
    for m in range(len(x_continuous)):
        if (x_continuous[m] >= x_segmented[n] and x_continuous[m] < x_segmented[n+1]):
            line_sigmoid = (slopes_sigmoid_POT[n] * x_continuous[m]) + lat_sigmoid_POT[n] + beta_seg[n] - (slopes_sigmoid_POT[n] * x_segmented[n])
            y_sigmoid_n.append(line_sigmoid)

line_sigmoid_last = (slopes_sigmoid_POT[-1] * x_continuous[-1]) + lat_sigmoid_POT[-1] + beta_seg[-1] - (slopes_sigmoid_POT[-1] * x_segmented[-1])
y_sigmoid_n.append(line_sigmoid_last)

lat_sigmoid_POT_beta = [(a + b) for a, b in zip(lat_sigmoid_POT, beta_seg)]

###################################################################################
# MSE and MAE calculations
###################################################################################
sq_diff_sigmoid_POT = (y_sigmoid - y_sigmoid_n)**2
mse_diff_sigmoid_POT  = np.mean(sq_diff_sigmoid_POT)

abs_diff_sigmoid_POT = np.abs(y_sigmoid - y_sigmoid_n)
mae_diff_sigmoid_POT  = np.max(abs_diff_sigmoid_POT)

###################################################################################
# Print results
###################################################################################
print("Data Format : FXP" + str(bw_total))
print("Total Points: " + str(2**bw_total))
print("Segments    : " + str(2**bw_segment))
print("Interval    : (-" + str(x_interval) + "," + str(x_interval) + ")")
print("MSE         : {:.2E}".format(mse_diff_sigmoid_POT))
print("MAE         : {:.2E}".format(mae_diff_sigmoid_POT))
print()
print("POT of slopes      :", slopes_sigmoid_POT[:-1])
print("Y-intercepts for \U0001D6FC :", lat_sigmoid_POT[:-1])
print("Y-intercepts for \U0001D6FD :", lat_sigmoid_POT_beta)

###################################################################################
# Plot results
###################################################################################
# Create subplots with shared x-axis
fig, (ax1) = plt.subplots(1, 1, figsize=(10, 5), sharex=True)

# Subplot 1 for sigmoid
ax1.plot(x_continuous, y_sigmoid, label='Sigmoid Original', linestyle='-', color='blue')
ax1.plot(x_continuous, y_sigmoid_i, label='Sigmoid Base', linestyle='--', color='green')
ax1.plot(x_continuous, y_sigmoid_n_alpha, label='Sigmoid Alpha', linestyle='dashdot', color='black')
ax1.plot(x_continuous, y_sigmoid_n, label='Sigmoid Beta', linestyle='dotted', color='red')
ax1.set_ylabel('Sigmoid Output', color='black')
ax1.set_xlabel('x Input', color='black')
ax1.tick_params('y', colors='black')

# Create a second y-axis on the right for squared differences
# ax1_twin = ax1.twinx()
# ax1_twin.plot(x_continuous, sq_diff_sigmoid_POT, label='Sigmoid square difference', linestyle='-', color='red')
# # ax1_twin.plot(x_continuous, abs_diff_sigmoid_POT, label='Sigmoid absolute difference', linestyle='-', color='red')
# ax1_twin.set_ylabel('Sigmoid Mean Square Error', color='black')
# ax1_twin.tick_params('y', colors='black')

# Add legends for subplot 1
lines1, labels1 = ax1.get_legend_handles_labels()
# lines1_twin, labels1_twin = ax1_twin.get_legend_handles_labels()
ax1.legend(lines1, labels1)
# ax1.legend(lines1 + lines1_twin, labels1 + labels1_twin)

# Add a grid for both y-axes in subplot 1
ax1.grid(True, which='both', axis='both')

# Display the plot
title_str = "Semi-sigmoid with " + str(x_seg_points) + " segments"
plt.title(title_str)
fig.tight_layout()
plt.show()
