a=int(input("Enter a number "))
c=0
for i in range(2,a):
	if(a%i==0):
		c=1
if(c==1):
	print(a,"is not prime")
else:
	print(a,"is prime")