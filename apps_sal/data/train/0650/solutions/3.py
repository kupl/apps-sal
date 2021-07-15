# cook your dish here
# cook your dish here
def cal(a):
    
    a.sort(key=lambda x:x[1])
    len1=len(a)
    c=1
    curr=a[0][1]
    for p in range(0,len1-1):
        if curr<=a[p+1][0]:
            c+=1
            curr=a[p+1][1]
    return c
    
    
    
t=int(input())
for i in range(t):
    n,k=list(map(int,input().split()))
    list1=[]
    a=[]
    count=0
    for j in range(n):
        s,f,p=list(map(int,input().split()))
        list1.append((s,f,p))
    list1.sort(key=lambda x:x[2])
    for j in range(0,n-1):
        if list1[j][2]==list1[j+1][2] and j!=n-2:
            a.append((list1[j][0],list1[j][1]))
        elif list1[j][2]==list1[j+1][2] and j==n-2:
            a.append((list1[j][0],list1[j][1]))
            a.append((list1[j+1][0],list1[j+1][1]))
            
            count+=cal(a)
            a=[]
        elif list1[j][2]!=list1[j+1][2] and j==n-2:
            a.append((list1[j][0],list1[j][1]))
            count+=cal(a)
            a=[]
            a.append((list1[j+1][0],list1[j+1][1]))
            count+=cal(a)
            a=[]
        else:
            a.append((list1[j][0],list1[j][1]))
            count+=cal(a)
            a=[]
    print(count)

