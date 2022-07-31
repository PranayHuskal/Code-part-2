

#Q.6 Write a program which accept one number & display below pattern.
#  input:5                *  *  *  *  *
#                         *  *  *  *  
#                         *  *  *  
#                         *  *  
#                         *  
b= int(input("Enter a number of rows : "))
for i in range(b,0,-1):
	print(" * "*i)
