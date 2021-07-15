N = int(input())
c = 0
for _ in range(N):
 p = list(map(int,input().split()))
 s = p.count(1)
 if(s>=2):
  c+=1
print(c)

