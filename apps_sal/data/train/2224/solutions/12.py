a=0
b=0
c=0
d=0
n=int(input())
s=input()
t=input()
for i in range(n):
    if s[i]=='0' and t[i]=='0':
        a+=1
    elif s[i]=='0' and t[i]=='1':
        b+=1
    elif s[i]=='1' and t[i]=='0':
        c+=1
    elif s[i]=='1' and t[i]=='1':
        d+=1
print(a*(c+d)+b*c)
