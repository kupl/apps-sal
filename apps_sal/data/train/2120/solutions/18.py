n = int(input())
t = 1
a = [0]
p = [0] * (n + 2)
s = 0

ans = [0] * n
for i in range(n):

    m = list(map(int, input().split()))
    if len(m) == 1:

        s -= (p[t - 1] + a[-1])
        t -= 1
        p[t - 1] += p[t]
        p[t] = 0

        a.pop(-1)
    elif len(m) == 2:
        a.append(m[1])
        s += m[1]
        t += 1

    else:
        s += m[1] * m[2]
        p[m[1] - 1] += m[2]
    ans[i] = str(s / t)
print("\n".join(ans))
