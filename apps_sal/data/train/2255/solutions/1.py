maxn = int(3e5) + 3
maxa = (1 << 20) + 3
nb_element = int(input())
arr = [int(x) for x in input().split()]
cnt = [[0 for _ in range(maxa)] for _ in range(2)]
cnt[1][0] = 1
xors = 0
res = 0
for i in range(nb_element):
    xors ^= arr[i]
    x = i % 2
    res += cnt[x][xors]
    cnt[x][xors] += 1
print(res)
