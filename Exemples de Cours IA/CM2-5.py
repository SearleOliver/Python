import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

n ,a , b = 100 ,2 ,3
expectation = ( a + b ) /2
deviation = (b - a ) / np . sqrt (12* n )
n_realisations = 100000
x_average_sample = np . array ([
np . average ( np . random . uniform (2 ,3 , n ) )
for _ in range ( n_realisations )
])
x_average_sample =( x_average_sample - expectation ) / deviation
x_bins = np . linspace ( -5 ,5 , int ( np . sqrt ( n_realisations ) ) )
plt . hist ( x_average_sample , bins = x_bins , density = True )
plt . plot ( x_bins , np . vectorize ( st . norm . pdf ) ( x_bins ) )
plt . show ()