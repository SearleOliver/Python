import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

# Attention a maitriser la portee de mu et sigma
def f_normal ( x ) :
    return st . norm . pdf (x , mu , sigma )

n = 10000
mu , sigma = 3 ,2
x_sample = np . random . normal ( mu , sigma , n )
x_bins = np . linspace ( -5 ,13 , int ( np . sqrt ( n ) ) )
plt . hist ( x_sample , bins = x_bins , density = True )
plt . plot ( x_bins , np . vectorize ( f_normal ) ( x_bins ) )
plt . show ()