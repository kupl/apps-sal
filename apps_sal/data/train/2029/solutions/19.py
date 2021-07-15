n=int(input())
arr=[0]*(2*n)
print("NYOE S"[n%2::2])
if(n%2!=0):
 for i in range(n):
    if(i%2==0):arr[i]=2*i+1;arr[i+n]=arr[i]+1
    else:arr[i]=2*i+2;arr[i+n]=arr[i]-1
 print(*arr)

