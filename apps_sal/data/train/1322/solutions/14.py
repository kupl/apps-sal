for _ in range(int(input())):
 # n = int(input())
 n,k = list(map(int,input().split()))
 s = sorted(map(int,input().split()),reverse=True)
 while k<n and s[k-1] == s[k] :
  k += 1
 print(k)

