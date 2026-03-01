import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

def confidence_interval ( confidence , average , unbiased_s , n ) :
    alpha_div_2 = (1 - confidence ) /2
    zoro = st . norm . ppf (1 - alpha_div_2 )
    delta = zoro * unbiased_s / np . sqrt ( n )
    return ( average - delta , average + delta )

print ( confidence_interval (0.95 ,145.2 ,23.7 ,92) )


n ,a , b = 1000 ,2 ,3
confidence = 0.99

mu = ( a + b ) /2 # unkown
draws = []
for _ in range (10000) :
    x_sample = np . random . uniform (a ,b , n )
    average = np . average ( x_sample )
    unbiased_s = np . std ( x_sample , ddof =1)
    low , high = confidence_interval ( confidence , average , unbiased_s, n)
    draws . append ( low <= mu <= high )
    
print ( np . average ( draws ) )
