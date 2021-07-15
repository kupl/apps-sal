# cook your dish here
a=[]
for x in range(0,12):
    a.append(2**x)
    
for y in range(int(input())):
    n=int(input())
    if n%2==0:
        k=0
    else:
        k=1
    while n!=1 and n!=0:
        for x in range(11,0,-1):
            if n==a[x]:
                k+=1
                n=0
                break
            elif a[x]<n:
                n-=a[x]
                k+=1
                break
    print(k)
    

