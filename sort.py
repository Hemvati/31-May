l1=[]
l2=[]
a=[]
s=int(input("Enter the size of list:"))
for i in range(s):
	e=int(input("Enter element:"))
	a.append(e)
print(a)
for num in a:
	if (num%2==0):
		l1.append(num)
	else:
		l2.append(num)
print(l1)
print(l2)


