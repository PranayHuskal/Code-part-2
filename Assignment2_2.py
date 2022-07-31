#Q.2 Write a program which accept one number & display below pattern.
#  input:5                *  *  *  *  *
#                         *  *  *  *  *
#                         *  *  *  *  *
#                         *  *  *  *  *
#                         *  *  *  *  *

a= int(input("Enter a number of rows : "))
for i in range(a):
	for j in range(a):
		print(" * ",end=" ")
	print()
# OR
a= int(input("Enter a number of rows : "))
for i in range(a):
	print(" * "*a)
