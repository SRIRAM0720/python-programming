a=raw_input("")
b=raw_input("")
c=raw_input("")
if isinstance(a,str) and isinstance(b,str) and isinstance(c,str):
    if(a.isalpha()) and (b.isalpha()) and (c.isalpha()):
        print("Invalid input")
    else:
        a=int (a)
        b=int (b)
        c=int (c)
        if(b<a>c):
            print("a is Greater")
        elif(a<b>c):
            print("b is Greater")
        else:
            print("c is greater")
