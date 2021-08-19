n = int(input())
a = list(map(int, input().split()))
a.sort()
a = a[::-1]
s = set()
signal = False
for x in range(n):
    if not signal:
        for y in range(x + 1, n):
            if not signal:
                for z in range(y + 1, n):
                    if a[x] + a[y] > a[z] and a[x] + a[z] > a[y] and (a[y] + a[z] > a[x]):
                        l = [a[x], a[y], a[z]]
                        signal = True
                        break
if signal:
    print('YES')
    print(l[0], l[1], l[2])
else:
    print('NO')
