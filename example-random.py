import random
l1=[]
n=int(input("Enter a number from 1 to 20:"))
for i in range(n):
	l1.append(random.randint(1,21))
print("Randomized list is",l1)


