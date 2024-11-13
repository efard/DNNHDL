# DNNHDL
## Introduction
The initial aim of this project is to simplify VHDL code generation for DNNs. In this repo, you will learn how to generate a `.vhd` file for Sigmoid and Tanh functions with the help of Python language. It is somehow a way of Piecewise Linear Approximation (PLA).

## Prerequisites
Install Python (The newer, the better!).

## Steps
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
You can play with Arbitrary inputs and get your own VHDL file for PLA.
### NB: If you find this project useful, I would appreciate it if you cited this repo. I will also be happy to hear any suggestions to improve this repo.
