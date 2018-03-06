#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 13:34:13 2018

@author: richardt
"""
#filename /Users/richardt/Desktop/UMASS/Applied Math MS project/Data Set/Full-Data-Set/Tissue Mechanical Testing/acl

#experimental vpython




import numpy as np
from matplotlib import pyplot as plt
import sys

def Stress(FD1, FD2):
    
    return 660*(FD2-FD1)
    

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
    t = np.array(t).astype(float)
    FDC = np.array(FDC).astype(float)
    FD = np.array(FD).astype(float)
    FFC = np.array(FFC).astype(float)
    FF = np.array(FF).astype(float)
    FC = np.array(FC).astype(float)
    CO = np.array(CO).astype(float)
    CC = np.array(CC).astype(float)
    return t, FDC, FD, FFC, FF, FC, CO, CC



t, FDC, FD, FFC, FF, FC, CO, CC = readData("/Users/richardt/Desktop/UMASS/Applied Math MS project/Data Set/Full-Data-Set/Tissue Mechanical Testing/acl/acl_stepstress.csv")
t2, FDC2, FD2, FFC2, FF2, FC2, CO2, CC2 = readData("/Users/richardt/Desktop/UMASS/Applied Math MS project/Data Set/Full-Data-Set/Tissue Mechanical Testing/acl/acl_preload.csv")


strtensor = np.zeros(len(FF))
#
strtensor = strtensor.T
    
#!!!!************position in excell - 6***********!!!

#stress calculation#
# @ 101.48535, FD[60] = 13.107944, Change = 0.243828, Force Change = 0.1607188375 N

# Using young's modulus
#=> 660 = x/(0.243828) means stress is 160.926 N/m^2
    
    
    
#stress at any given state
ST = np.zeros(len(FD))

for i in range(1,242914):
    ST[i]= 660*np.abs((FD[i]-FD[i-1]))



#Parameters
aclwidth = 2 #mm
acllength = 12.86 #mm
stress = FF/ (aclwidth*FD)
strain= (FD-FD[1])/FD[1]
ym = 19.6 #Young's modulus
stress2 = ym * strain



#******************writing outputs to file***




#To write the file used for MATLAB...
systy=np.zeros((len(t),8))
for i in range(len(systy)):
    systy[i]=t[i], FDC[i], FD[i], FFC[i], FF[i], FC[i], CO[i], CC[i]
    #make data set into .txt file...
    #with open ('MathDatatxt','w') as f:
        
        
        #f.write(str(systy)+'\n')


#!!!!!!np.savetxt('MathDatatxt.txt',np.around(systy,decimals=8))#save file

plt.figure()
plt.plot(t,stress2, marker='.', markersize='1', color='r', label="stress")
plt.legend()
#plt.xlim(left=29)
plt.xlabel("time")
plt.ylabel("Stress")
plt.show()

plt.figure()
plt.plot(strain,stress, marker='.', markersize='1', color='r', label="stress")
plt.legend()
#plt.xlim(left=29)
plt.xlabel("strain")
plt.ylabel("Stress")
plt.show()

plt.figure()
plt.plot(t,stress, marker='.', markersize='1', color='r', label="stress")
plt.legend()
#plt.xlim(left=29)
plt.xlabel("t")
plt.ylabel("Stress")
plt.show()

plt.figure()
plt.plot(t, FD, marker='.', markersize='1', color='k', label="stepstress")
plt.plot(t2, FD2, marker='.', markersize='1', color='r', label="preload")
plt.legend()
plt.xlabel("Time (sec)")
plt.ylabel("Frame Displacement (mm)")
#plt.xlim([0,1000])
plt.show()
#plt.close()

plt.figure()
plt.plot(FD, FF, marker='.', markersize='1', color='k', label="stepstress")
plt.plot(FD2, FF2, marker='.', markersize='1', color='r', label="preload")
plt.legend()
plt.xlabel("Frame Displacement (mm)")
plt.ylabel("Frame Force (N)")
plt.show()
#plt.close()

plt.figure()
plt.plot(FDC, FD, marker='.', markersize='1', color='k', label="stepstress")
plt.legend()
plt.xlabel("Frame Displacement Command (mm)")
plt.ylabel("Frame Displacement (mm)")
plt.show()
plt.close()



