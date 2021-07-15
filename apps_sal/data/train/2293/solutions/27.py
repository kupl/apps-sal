N = int(input())
A = list(map(int, input().split()))
f = [[a, -1] for a in A]
lim = 1<<N
for i in range(N):
    bit = 1<<i
    j = 0
    while j < lim:
        j |= bit
        a, b = f[j]
        c, d = f[j^bit]
        if a < c:
            f[j][0] = c
            f[j][1] = d if d>a else a
        elif b < c:
            f[j][1] = c
        j += 1
ans = sum(f[1])
Ans = [ans]
for a, b in f[2:]:
    s = a+b
    if s > ans:
        ans = s
    Ans.append(ans)
print(("\n".join(map(str, Ans))))

