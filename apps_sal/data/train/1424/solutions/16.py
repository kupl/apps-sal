na = list(map(int,input().split()))
n = na[0]
a = na[1]

n = str(n)
n = list(map(int,n))
for i in range(a):
 if n[-1] == 0:
  n.pop()
 else:
  n[-1] -= 1

print(int(''.join(list(map(str,n)))))

