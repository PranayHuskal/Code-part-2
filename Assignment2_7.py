

#Q.7 Write a program which accept one number & display below pattern.
# input: 5        1  2  3  4  5
#                 1  2  3  4  5 
#                 1  2  3  4  5
#                 1  2  3  4  5
#                 1  2  3  4  5

a= int(input("enter a number: "))
for i in range(1,a+1,1):
	for j in range(1,a+1,1):
		print(j,end=" ")
	print()
