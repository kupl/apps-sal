for _ in range(int(input())):
 n=int(input())
 a=[int(i) for i in input().split()]
 n-=a.count(0)
 n-=a.count(1)
 p=a.count(2)
 n-=p
 print(((n*(n-1))//2)+p*n)
