s=input()
t=input()
a=s.count('1')
b=t.count('1')
if a%2==0:
    if b<=a:
        print("YES")
    else:
        print("NO")
else:
    if b<=a+1:
        print("YES")
    else:
        print("NO")                
