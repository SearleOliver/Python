import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

n = 1000
n_realisations = 100000
x_average_sample = np . array ([
    np . average ( np . random . uniform (2 ,3 , n ) )
    for _ in range ( n_realisations )
])
x_bins = np . linspace (2 ,3 , int ( np . sqrt ( n_realisations ) ) )
plt . hist ( x_average_sample , bins = x_bins , density = True )
plt . show ()