import statsmodels.api as sm

x_sample = [149 ,156 ,157 ,168 ,169 ,176 ,182 ,183]
y_sample = [ 45 , 51 , 72 , 78 , 63 , 85 , 71 , 95]

x_sample = sm.add_constant ( x_sample )
model = sm.OLS ( endog = y_sample , exog = x_sample )
model_fit = model.fit ()
print ( model_fit.summary () )