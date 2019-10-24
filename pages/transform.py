# Transformation script

"""
This script contains the transformation function used to put the lightcurve
data into acceptable format for the machine learning model. You must use this
particular transformation in order to get a reliable prediction.
"""
import sklearn as skl
import pandas as pd
import numpy as np 
import scipy as spy 

def ft(x):
    y = spy.fft(x, n= x.size)
    return np.abs(y)

def transform_new(X):
    X = X.copy()
    
    # Normalize the new data
    mean = X.sum(axis=1) / len(X.columns)
    X = X.subtract(mean, axis=0)
    X = pd.DataFrame(skl.preprocessing.normalize(X))
    
    # Apply the FFT
    X = X.apply(ft, axis=1)
    
    # Re-format and split to correct length
    X = pd.DataFrame.from_records(X.iloc[[x for x in range(len(X))]])
    size = len(X.columns) - 1599
    X = X.loc[:,size:]
    
    # Provide uniform names for the column heads
    for i in range(len(X.columns)):
        X = X.rename(columns={X.columns[i]: f'f.{i+1}'})
        
    return X