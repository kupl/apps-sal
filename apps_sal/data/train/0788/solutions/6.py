a=int(input(""))
A=[]
for m in range(a):
    x=int(input(""))
    A.append(x)
for m in range(a):
    b=str(A[m])
    c=int(b[0])+int(b[(len(b)-1)])
    print(c)
