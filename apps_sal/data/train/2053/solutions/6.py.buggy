nBoys, nGirls = map(int, input().split())
boys = sorted(map(int, input().split()), reverse=True)
girls = sorted(map(int, input().split()))
if boys[0] > girls[0]:
    print(-1)
    return
ret = sum(girls)
for i in range(1, nBoys):
    ret += boys[i] * nGirls
if boys[0] != girls[0]:
    ret -= girls[0] - boys[0]
    ret += girls[0] - boys[1]
print(ret)
