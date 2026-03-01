import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

# Attention a maitriser la portee de a et b
def f_uniform ( x ) :
    return st . uniform . pdf (x ,a ,b - a )

a , b = 2 ,3
n = 10000
x_sample = np . random . uniform (a ,b , n )
x_bins = np . linspace (0 ,5 , int ( np . sqrt ( n ) ) )
plt . hist ( x_sample , bins = x_bins , density = True )
plt . plot ( x_bins , np . vectorize ( f_uniform ) ( x_bins ) )
plt . show ()