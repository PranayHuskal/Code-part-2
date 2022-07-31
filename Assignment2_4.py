
#Q.4  Write a program which accept one number & return addition of its factorial.

n = int(input("enter a number: "))
i=1
sum=0
while(i<=n):
	if(n%i==0):
		sum=sum+i
	i+=1
print("Addition of its factorial of ",n,'is: ',sum)

