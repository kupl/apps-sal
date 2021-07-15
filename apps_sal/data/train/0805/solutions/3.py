for _ in range(int(input())):
 n = int(input())
 arr =[0]*n
 for i in range(n):
  s,p,v = list(map(int,input().split()))

  arr[i] = (p//(s+1))*v
 print(max(arr)) # cook your dish here

