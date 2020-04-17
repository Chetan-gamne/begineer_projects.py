a=input("Enter the value")
b=list(a)
c=len(b)
d=[]
for i in range(c-1,-1,-1):
	d.append(b[i])
print(d)
sum=''
for i in range(c):
	sum=sum+str(d[i])
print(sum)	

