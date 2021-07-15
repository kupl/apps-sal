# cook your dish here
t=int(input())
for i in range(0,t):
    p=input()
    l=list(p)
    for j in range(0,len(l)):
        l[j]=int(l[j])
        l[j]=l[j]-2
    for j in range(0,len(l)):
        l[j]=str(l[j])
    q=''.join(l)
    print(q)
