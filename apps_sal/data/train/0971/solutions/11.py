# cook your dish here
for _ in range(int(input())):
 n=int(input())
 arr=list(map(int,input().split()))
 m=0
 s=list(set(arr))
 for i in range(len(s)):
  m=max(m,arr.count(s[i]))
 print(n-m)
