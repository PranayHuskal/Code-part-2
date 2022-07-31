 
#Q.5 Write a program which accept one number from user & check whether number is prime or not.

n= int(input("enter a number: "))

for j in range(2,n):
		if(n%j)==0:
			print(n,'is  not prime number')
			break
else:
		print(n," is prime number")


