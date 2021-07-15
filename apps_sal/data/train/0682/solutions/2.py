n=int(input())
l=[int(x) for x in input().split()]
left, right, i, num, flag=0, 0, 0, 0, 0
while(i<n):
    if(l[i]!=i+1):
        num=l[i]
        i+=1
        left=i
        flag+=1
        while(i<n and abs(l[i]-num)==1):
            num=l[i]
            i+=1
        right=i
    else:
        i+=1
if(flag==1):
    print(left, right, sep=" ")
else:
    print("0 0")
