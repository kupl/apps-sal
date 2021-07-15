# cook your dish here
n,sal,tip=list(map(int,input().split()))
a=list(map(int,input().split()))
res=n*sal
for i in range(len(a)):
    num=a[i]-1
    res+=(tip-(tip*2*num/100))
#print(res)    
if res<300:
    print("NO")
else:
    print("YES")

