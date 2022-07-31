
#Q.9 Write a program which accept one number & return number of digits in that number.

a= int(input("enter a number: "))
count=0

if a<0:
	a = -1 * a 
if a ==0:
	count=1

while(a!=0):
	a = a//10
	count+=1
print('number of digits : ',count)

