for _ in range(int(input())):
 N=int(input())
 arr=list(map(int,input().split()))
 arr.sort()
 sum=0
 for i in range(1,len(arr)):
  sum+=arr[i]*arr[0]
 print(sum)
