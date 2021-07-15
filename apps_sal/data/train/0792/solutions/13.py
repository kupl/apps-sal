# cook your dish here
x=7+10**9
for i in range(int(input())):
    n,s=input().split()
    n=int(n)
    l=len(s)
    if n>l:
     p=pow(26,n-l-1,x)
     p*=(25*l+26)
     print(p%x)
    else:print("0")
 

