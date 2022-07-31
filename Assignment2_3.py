#Q.3 Write a program which accept one number & return its factorial.

a =int(input("enter a number: "))
fact=1

while(a>0):
	fact= fact*a
	a-=1
print("Factorial: ",fact)

