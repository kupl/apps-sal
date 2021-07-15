n=int(input())
for i in range(n):
 t = int(input())
 l=list(map(int,input().split()))
 l.sort()
 print(l[0]+l[1])
