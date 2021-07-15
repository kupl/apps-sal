for _ in range(int(input())):
 N=int(input())
 arr=list(map(int,input().split()))
 s=[]
 for i in range(len(arr)):
  s.append(arr[i]+i)
 print(max(s))
