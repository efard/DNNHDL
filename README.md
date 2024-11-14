# DNNHDL
## Introduction
This project's initial aim is to simplify VHDL code generation for DNNs. It now covers two techniques for generating hardware-efficient `.vhd` codes for prevalent Activation Functions (AFs), i.e. Sigmoid and Tanh.

In the first section, you will learn how to generate a `.vhd` file for Sigmoid and Tanh functions with Python language. This strategy is based on LUT-based AFs and the main functions are transformed to some horizontal lines. The second section is more advanced and based on Piecewise Linear (PWL) approximation technique. at which nonlinear AFs are converted to som

## Prerequisites
Install Python (The newer, the better!).

##LUT-based Activation Functions

### Steps
1. Clone the project in a folder and open it.
2. Set your values in the "Arbitrary inputs" section of the "sig_tanh_gen.py" file.
3. Run (in Windows):\
py .\sig_tanh_gen.py\
Or (in Linux):\
python3 sig_tanh_gen.py\

With default inputs, you will see results similar to Fig. 1\
\
![Fig_1](https://user-images.githubusercontent.com/43655559/201485061-c8a6c6ea-5281-4e9f-9c5f-31f642b409bf.png)\
Also, you can see “generated_sig.vhd” and “generated_tanh.vhd” files in current folder.\
You can play with Arbitrary inputs and get your custom VHDL file for PLA.
### NB: If you find this project useful, I would appreciate your citing this repo. I will also be happy to hear any suggestions for improving this repo.
