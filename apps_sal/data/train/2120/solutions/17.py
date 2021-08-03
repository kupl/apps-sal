n = int(input())
s = 0
c = 1
l = [0]
d = [0]
ans = [0] * n
for i in range(n):
    x = list(map(int, input().split()))
    if x[0] == 1:
        d[x[1] - 1] += x[2]
        s = s + x[1] * x[2]
    elif x[0] == 2:
        l.append(x[1])
        d.append(0)
        s = s + x[1]
        c = c + 1
    else:
        t = d[-1]
        s = s - l[-1] - t
        c = c - 1
        l.pop()
        d.pop()
        d[-1] += t
    ans[i] = str(s / c)
print('\n'.join(ans))
