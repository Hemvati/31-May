s=str(input("Enter a string with blank spaces:"))
for i in s:
	if (i==' '):
		print('Modified string  is:',s.replace(' ','-'))
