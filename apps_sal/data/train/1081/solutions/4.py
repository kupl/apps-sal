# cook your dish here
t=int(input())
l=[98,57,31,45,46]
for _ in range(t):
    s=input().strip().upper()
    a=65
    z=''
    for i in range(len(s)):
        x=ord(s[i])-a
        x+=l[i]
        x%=26
        z+=chr(x+a)
    print(z)
        

