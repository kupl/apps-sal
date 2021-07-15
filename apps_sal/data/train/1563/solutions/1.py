for _ in range(int(input())):
 n,m=input().split()
 n=int(n[::-1])
 m=int(m[::-1])
 ans=str(n+m)[::-1]
 print(int(ans))
