# cook your dish here
n=int(input())
a=[]
for i in range (0,n):
    no=int(input())
    a.append(no)
for i in range (0,n):
    s=0
    while (a[i]!=0):
        c=a[i]%10
        s=s+c
        a[i]=a[i]//10
    print(s)
    

