import numpy as np

def r2_score ( labels , predictions ) :
    return (1 - sum (( labels - predictions ) **2)/ sum (( labels - np.average ( labels ) ) **2))


x_sample = [149 ,156 ,157 ,168 ,169 ,176 ,182 ,183]
y_sample = [ 45 , 51 , 72 , 78 , 63 , 85 , 71 , 95]

a , b = np.polyfit ( x_sample , y_sample ,1)
predictions = np.polyval ([ a , b ] , x_sample )
print ( r2_score ( y_sample , predictions ) )