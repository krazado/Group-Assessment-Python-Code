#Final regresion equation, we use it to find out revenue 
#Revenue = 4.3976 + (1.5998×MAN) − (0.4364×INCOME) + (1.0901×TYP) 

# Given values
MAN = [1,2,3,4,5,6,7,8,9] 
INCOME = [8000, 14000]
TYP = [0, 1] 

# Coefficients from the regression equation
intercept = 4.3976
coef_MAN = 1.5998
coef_INCOME = -0.4364
coef_TYP = 1.0901
st_error = 0.91

# Plug the values into the equation
revenue = intercept + (coef_MAN * MAN[0]) + (coef_INCOME * INCOME[0]) + (coef_TYP * TYP[0]) - (2 * st_error)

print("Predicted revenue:", revenue / 1000000)