d, x, y = list(map(int,input().split()))
l = list(map(int,input().split()))

k = [y]

for i in range(6):
    k.append(k[-1]*0.98)


s = x*d

for i in l:
    s += k[i-1]

if s >= 300:
    print("YES")
else:
    print("NO")

