
import numpy as np
from matplotlib import pyplot as plt
import sys


def readData(filename):
    t, FDC, FD, FFC, FF, FC, CO, CC = [], [], [], [], [], [], [], []
    """
        Variables / units are:
        t = time (sec)
        FCD = Frame Displacement Command (mm)
        FD = Frame Displacement (mm)
        FFC = Frame Force Command (N)
        FF = Frame Force (N)
        FC = Frame Count (cycles)
        CO = Camera Output (V)
        CC = Camera Count (cycles)
    """
    line_num = 0
    with open(filename) as data:
        for l in data:
            if line_num == 0:
                quote = l[0] # capture the quotation mark to use as a check for a line of just text later
            if not l.isspace(): # If line is not blank
                if l[0] != quote: # If the line doesn't start with text
                    row = l.split()
                    t.append(row[0])
                    FDC.append(row[1])
                    FD.append(row[2])
                    FFC.append(row[3])
                    if row[4][0] == quote: # catch the annoying quotes for scientific notation in frame forces
                        tmp = row[4]
                        new = ''.join(tmp.split(quote,1)) # removes the first time quote is encountered
                        new = ''.join(new.split(quote,1)) # removes the second time the quote is encountered
                        FF.append(new)
                    else:
                        FF.append(row[4])
                    FC.append(row[5])
                    CO.append(row[6])
                    CC.append(row[7])
            line_num = line_num + 1
    t = np.array(map(float, t))
    FDC = np.array(map(float, FDC))
    FD = np.array(map(float, FD))
    FFC = np.array(map(float, FFC))
    FF = np.array(map(float, FF))
    FC = np.array(map(float, FC))
    CO = np.array(map(float, CO))
    CC = np.array(map(float, CC))
    return t, FDC, FD, FFC, FF, FC, CO, CC



t, FDC, FD, FFC, FF, FC, CO, CC = readData("Multiscaledataset-latest/Tissue Mechanical Testing/acl/acl_stepstress.csv")
t2, FDC2, FD2, FFC2, FF2, FC2, CO2, CC2 = readData("Multiscaledataset-latest/Tissue Mechanical Testing/acl/acl_preload.csv")

plt.figure()
plt.plot(t, FD, marker='.', markersize='1', ls='none', color='k', label="stepstress")
plt.plot(t2, FD2, marker='.', markersize='1', ls='none', color='r', label="preload")
plt.legend()
plt.xlabel("Time (sec)")
plt.ylabel("Frame Displacement (mm)")
#plt.xlim([0,1000])
plt.show()
#plt.close()

plt.figure()
plt.plot(FD, FF, marker='.', markersize='1', ls='none', color='k', label="stepstress")
plt.plot(FD2, FF2, marker='.', markersize='1', ls='none', color='r', label="preload")
plt.legend()
plt.xlabel("Frame Displacement (mm)")
plt.ylabel("Frame Force (N)")
plt.show()
#plt.close()

plt.figure()
plt.plot(FDC, FD, marker='.', markersize='1', ls='none', color='k', label="stepstress")
plt.legend()
plt.xlabel("Frame Displacement Command (mm)")
plt.ylabel("Frame Displacement (mm)")
plt.show()
plt.close()

