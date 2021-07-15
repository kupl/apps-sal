n = int(input())
arr = list(map(int,input().split()))
i,j = 0,n-1
x,y = -1,-1
while i<j:
    if arr[i]==i+1 and x<0: i+=1
    else: x=i
    if arr[j]==j+1 and y<0: j-=1
    else: y=j
    if x>=0 and y>=0: break
if arr[i:j+1][::-1]==list(range(x+1,y+2)):
    print(x+1,y+1)
else:
    print(0,0)
