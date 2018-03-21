# your code goes here
a=raw_input("")
b=raw_input("")
c=raw_input("")
if isinstance(a,str) and isinstance(b,str) and isinstance(c,str):
	if(a.isalpha()) and (b.isalpha()) and (c.isalpha()):
		print("invaild input")
	else:
		a=int (a) 
		b=int (b)
		c=int (c)
		if((b<a) and (a>c)):
		    print("a is greater")
		elif((a<b) and (b>c)):
		    print("b is greater")
		else:
		    print("c is greater")
