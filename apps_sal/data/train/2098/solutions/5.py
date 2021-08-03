def solve(max_v, votes, m):
    ans = 0
    values = []
    our_v = len(votes[0])
    for i in range(1, m):
        L = len(votes[i])
        if L > max_v:
            take = L - max_v
            our_v += take
            ans += sum(votes[i][:take])
            if take < L:
                values.extend(votes[i][take:])
        else:
            values.extend(votes[i])
    values.sort()
    if our_v <= max_v:
        needed = max_v + 1 - our_v
        if needed <= len(values):
            for i in range(needed):
                ans += values[i]
                our_v += 1
    if our_v <= max_v:
        return 1 << 60
    return ans


n, m = [int(x) for x in input().split()]
votes = [[] for x in range(m)]

for i in range(n):
    p, c = (int(x) for x in input().split())
    p -= 1
    votes[p].append(c)

for i in range(m):
    L = len(votes[i])
    if L > 1:
        votes[i].sort()
lo = 0
hi = n // 2 + 5
while lo < hi:
    mi = lo + (hi - lo) // 2
    if solve(mi, votes, m) > solve(mi + 1, votes, m):
        lo = mi + 1
    else:
        hi = mi
ans = 1 << 60
E = 20
for i in range(max(0, lo - E), min(lo + E, n + 1)):
    ans = min(ans, solve(i, votes, m))
print(ans)
