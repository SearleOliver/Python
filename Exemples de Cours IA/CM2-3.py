import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

# en bouclant
n = 100
for _ in range (20) :
    x_sample = np . random . binomial (1 ,0.3 , n )
    x_average = np . average ( x_sample )
    print ( x_average )