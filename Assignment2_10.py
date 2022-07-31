
#Q.10 Write a program which accept one number & return the addition of digits in that number.

a= int(input("enter a number: "))
sum=0

while(a>0):
	sum=sum+a%10                    # '%' returns the remainder
	a=a//10                         # '//' is used to not get digits after decimal point.
print('sum of digits: ',sum)

