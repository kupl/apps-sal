# cook your dish here
d,x,y=map(int,input().split())
arr=[int(i) for i in input().split()];s=x*d;arr1=[]
for i in range(6):
    arr1.append(i*2)
for i in arr:
    s=s+(y-(y*arr1[i-1]*2/100))
if s>=300:
    print("YES")
else:
    print("NO")
