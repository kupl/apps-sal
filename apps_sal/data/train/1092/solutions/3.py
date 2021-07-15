
for i in range(int(input())):
 n=list(map(int,input().split()))
 a = []
 for j in range(n[0]-1):
  a.append(sum(map(int,input().split())))

 re = sum(map(int, input().split()))

 a.sort(reverse=True)
 s = a[n[1] - 1]
 b = s - re + 1
 if b<0:
  print("0")
 elif b <=n[3]:
  print(b)
 else:
  print("Impossible")
