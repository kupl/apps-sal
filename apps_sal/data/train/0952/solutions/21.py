# cook your dish here
t= int(input())
for i in range (t):
    a= input()
    b=list()
    sum=0
    for i in a:
        d=ord(i)-96
        b.append(d)
    for i in b:
        z=[]
        d=[1,5,9,15,21]
        if i not in d:
            for p in d:
                x=abs(i-p)
                z.append(x)
            sum=sum+min(z)
    print(sum)
            
            
    

