t= int(input())
for _ in range(t):
 n=int(input())
 l = list(map(int,input().split()))
 a = n//4
 l.sort()
 if(l[a] == l[a-1] or l[2*a]==l[2*a-1] or l[3*a]==l[3*a-1]):
  print(-1)
 else:
  print(l[a],l[2*a],l[3*a])
