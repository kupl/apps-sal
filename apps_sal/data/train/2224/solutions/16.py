n=int(input())
a=input()
b=input()
x,y,z,w=0,0,0,0
""" w 00
    x 01
    y 10
    z 11 """
for i in range(n):
    if a[i]=='0':
        if b[i]=='0':
            w+=1
        else:
            x+=1
    else:
        if b[i]=='0':
            y+=1
        else:
            z+=1
print(w*(y+z) + y*x)
