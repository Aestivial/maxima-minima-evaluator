# import sympy
from sympy import *

x, y = symbols('x y')
expr = input("Enter the equation to be differentiated:    ")
print("Expression : {} ".format(expr))

# Use sympy.Derivative() method
expr_diff = Derivative(expr, x)
	
print("Derivative of expression with respect to x : {}".format(expr_diff))
print("Value of the derivative : {} ".format(expr_diff.doit()))

