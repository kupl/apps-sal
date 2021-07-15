# cook your dish here
n=int(input())
a=list(map(int, input().split()))
flag=0
x=0
y=0
for i in range(0,n-1):
    
    if(flag==0 and (abs(a[i+1]-a[i])!=1)):
        flag+=1
        x=a[i+1]
    elif(flag==1 and (abs(a[i+1]-a[i])!=1)):
        flag+=1
        y=a[i]
    elif(flag==2 and (abs(a[i+1]-a[i])!=1)):
        flag+=1
        break;
if(flag==2):
    print(y,x)
else:
    print("0 0")
