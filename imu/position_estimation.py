import os
import datetime
import csv
import scipy as sp
from scipy import integrate
from scipy import signal
import numpy as np
import pandas as pd


def calculate_delta(timestamp_1, timestamp_2):
    """
    Calculate the time delta between image captures 

    return: time delta (in s)
    """
    
    difference = timestamp_1 - timestamp_2
    delta = (difference.seconds * 1) + (difference.microseconds / 1000000)
    
    return delta


def convert_accelerometer(a, bias=0):
    return (a-bias) * 9.8


def numericalIntegration(y, dx):
    
    result = [0]
    for i in range(len(y)-1):
        result.append(
            result[i] + y[i+1]*dx
        )

    result.pop(0)
    return np.array(result)
