#!/usr/local/bin/python3

## Import various important packages
import numpy as np
import scipy.special as s
#import matplotlib.pylab as plt
#import argparse
import sys

# Set some parameters
meanP    = 0.0
sigmaP   = 1.0 
meanN    = 0.0
sigmaN   = 1.0
Tobs     = 10000 #time samples
Window   = 100
Tscrunch = 10

for val in range(1,100):
    for niter in range(0,100):

        pulsar = np.zeros(Tobs)
        noise    = np.random.normal(0,sigmaN,Tobs)
        for i in range(Tobs//2-Window//2, Tobs//2+Window//2): # Square pulse profile
            pulsar[i] = val*0.1
        signal = pulsar + noise
        signal     = (signal - np.mean(signal))/np.std(signal)
        # 1 bit
        signal1bit = signal.copy()
        for i in range(0,np.size(signal1bit)):
            if (signal1bit[i] >= 0.0):
                signal1bit[i] = 1
            else:
                signal1bit[i] = 0
        signal1bit = (signal1bit - np.mean(signal1bit))/np.std(signal1bit)
        # 2 bit
        signal2bit = signal.copy()
        for i in range(0,np.size(signal2bit)):
            # -1, 0, +1 --> -3/2 -1/2 +1/2 +3/2
            if (signal2bit[i] >= 1.0):
                signal2bit[i] = 1.5
            elif ((signal2bit[i] >= 0.0) and (signal2bit[i] < 1.0)):
                signal2bit[i] = 0.5
            elif ((signal2bit[i] >= -1.0) and (signal2bit[i] < 0.0)):
                signal2bit[i] = -0.5
            elif (signal2bit[i] < -1.0):
                signal2bit[i] = -1.5
        signal2bit = (signal2bit - np.mean(signal2bit))/np.std(signal2bit)
        area       = np.sum(signal    [Tobs//2-Window//2:Tobs//2+Window//2])
        area1bit   = np.sum(signal1bit[Tobs//2-Window//2:Tobs//2+Window//2])
        area2bit   = np.sum(signal2bit[Tobs//2-Window//2:Tobs//2+Window//2])
        print("%.1f %f %f"%((val*0.1),(area1bit/area),(area2bit/area)))

sys.exit()
