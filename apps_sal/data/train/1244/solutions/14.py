MOD = (10**9) + 7
N = int(input())
mapsb = {}
mapsd = {}
start = float("inf")
end = -float("inf")
for i in range(N):
    b, d = list(map(int, input().split()))
    mapsb[b] = mapsb.get(b, 0) + 1
    mapsd[d] = mapsd.get(d, 0) + 1
    start = min(b, d, start)
    end = max(b, d, end)
severity = 0
infectionDegree = 0
for i in range(start, end + 1):
    if i in mapsb:
        infectionDegree += mapsb[i]
    severity += infectionDegree
    if i in mapsd:
        infectionDegree -= mapsd[i]
print(severity % MOD)
