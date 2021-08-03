n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
m = int(input())
b = list([int(x) - 1 for x in input().split()])
c = []
now = 0
k = 0
ans = []
for i in range(n):
    t = a[i]
    if t[0] == 1:
        now += 1
        if len(c) < 100000:
            c.append(t[1])
        if k < m and b[k] == now - 1:
            ans.append(t[1])
            k += 1
    else:
        last = now
        now += t[1] * t[2]
        while t[2]:
            if len(c) < 100000:
                c.extend(c[:t[1]])
            else:
                break
            t[2] -= 1
        while k < m and last <= b[k] < now:
            ans.append(c[(b[k] - last) % t[1]])
            k += 1
print(' '.join(map(str, ans)))
