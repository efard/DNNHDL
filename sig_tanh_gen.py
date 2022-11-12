
import numpy as np
import matplotlib.pyplot as plt

#Arbitrary inputs#######################################################################
input_bitwidth   = 8
output_bitwidth  = 16
curve_factor     = 1    # for large values of "input_bitwidth" play with this variable :-)
saturation_value = 5    # "input" value in which the sigmoid function saturates

input_range = 2**input_bitwidth
output_max  = ((2**output_bitwidth)/2)-1

########################################################################################
###Sigmoid function generation##########################################################
########################################################################################
fh = open("generated_sig.vhd", "w")

string0 = "--sigmoid with saturation value: %d\n" % saturation_value
fh.write("\n" + string0)
fh.write("\nLIBRARY IEEE;\n")
fh.write("USE IEEE.std_logic_1164.ALL;\n")
fh.write("USE IEEE.numeric_std.ALL;\n\n")
fh.write("entity my_sigmoid is\n")
fh.write("    port (i_data: in  std_logic_vector(%d downto 0);\n" % (input_bitwidth-1))
fh.write("          o_data: out std_logic_vector(%d downto 0));\n" % (output_bitwidth-1))
fh.write("end my_sigmoid;\n\n")
fh.write("architecture Behavioral of my_sigmoid is\n\n")
fh.write("  signal s_temp : signed(%d downto 0);" % (input_bitwidth-1) + "\n\n")
fh.write("begin\n\n")
fh.write("  s_temp  <= signed(i_data);\n\n")
fh.write("  o_data  <= \n")

qx_vector = list()
qy_vector = list()

for i in range(input_range):
    qx = i-(input_range/2)
    rx = qx*curve_factor/(saturation_value/5)
    ry = 1/(1+np.e**-rx)
    qy = np.round(ry*output_max)
    if(qy > 0 and qy < output_max):
        string1 = "        std_logic_vector(to_signed(%d,8)) \twhen (s_temp = %d) \t else" % (qy, qx)  
        fh.write(string1 + "\n")
        qx_vector.append(qx)
        qy_vector.append(qy)
    elif(qy >= output_max):
        string1 = "        std_logic_vector(to_signed(%d,8)) \twhen (s_temp >= %d) \t else" % (output_max, qx)
        fh.write(string1 + "\n")
        break

fh.write("        std_logic_vector(to_signed(0,8)); \t--for small inputs\n")
fh.write("end Behavioral;\n")
fh.close()

########################################################################################
###Tanh function generation#############################################################
########################################################################################
fh = open("generated_tanh.vhd", "w")

string0 = "--tanh with saturation value: %d\n" % saturation_value
fh.write("\n" + string0)
fh.write("\nLIBRARY IEEE;\n")
fh.write("USE IEEE.std_logic_1164.ALL;\n")
fh.write("USE IEEE.numeric_std.ALL;\n\n")
fh.write("entity my_tanh is\n")
fh.write("    port (i_data: in  std_logic_vector(%d downto 0);\n" % (input_bitwidth-1))
fh.write("          o_data: out std_logic_vector(%d downto 0));\n" % (output_bitwidth-1))
fh.write("end my_tanh;\n\n")
fh.write("architecture Behavioral of my_tanh is\n\n")
fh.write("  signal s_temp : signed(%d downto 0);" % (input_bitwidth-1) + "\n\n")
fh.write("begin\n\n")
fh.write("  s_temp  <= signed(i_data);\n\n")
fh.write("  o_data  <= \n")

qxt_vector = list()
qyt_vector = list()

for i in range(input_range):
    qx = i-(input_range/2)
    rx = qx*curve_factor/(saturation_value/5)
    ry = ((np.e**rx)-(np.e**-rx))/((np.e**rx)+(np.e**-rx))
    qy = np.round(ry*output_max)
    if(qy > -output_max and qy < output_max):
        string1 = "        std_logic_vector(to_signed(%d,8)) \twhen (s_temp = %d) \t else" % (qy, qx)  
        fh.write(string1 + "\n")
        qxt_vector.append(qx)
        qyt_vector.append(qy)
    elif(qy >= output_max):
        string1 = "        std_logic_vector(to_signed(%d,8)) \twhen (s_temp >= %d) \t else" % (output_max, qx)
        fh.write(string1 + "\n")
        break

string2 = "        std_logic_vector(to_signed(-%d,8)); \t--for small inputs" % (output_max + 1)
fh.write(string2 + "\n")
fh.write("end Behavioral;\n")
fh.close()

########################################################################################
###Plot results#########################################################################
########################################################################################
fig, ax = plt.subplots()
ax.plot(qx_vector, qy_vector, 'g^', label='Sigmoid')
ax.plot(qxt_vector, qyt_vector, 'r--', label='Tanh')
plt.grid()
plt.legend()
plt.xlabel('Input Integer Values')
plt.ylabel('Output Quantized Values')
plt.title('Sigmoid & Tanh Functions')
plt.show()

