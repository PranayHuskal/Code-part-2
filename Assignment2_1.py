#Q.1 Create module named as Arithmetic which contaon four functions as Add() for addition,Sub() for substraction,Mult() for multiplication and Div() for division.
#    All functions accepts two parameters as number and perform the operation. Write on python program which call all the functions from arithmetic module by
#    accepting the parameters from user.

import Arithmetic                               # All functions are store in module name 'Arithmetic'
def main():
	a = int(input("Enter first number: "))
	b = int(input("Enter second number: "))
	
	print("Addition is : ",Arithmetic.Add(a,b))                 #Function importing from module Arithmetic.
	print("Substraction is : ",Arithmetic.Sub(a,b))
	print("Multiplication is : ",Arithmetic.Mult(a,b))
	print("Division is : ",Arithmetic.Div(a,b))

main()
