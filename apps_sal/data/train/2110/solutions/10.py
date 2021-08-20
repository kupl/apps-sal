n = int(input())
MAXN = 10 ** 6 + 20
bit = [0] * MAXN
for s in input().split(' '):
    ss = int(s)
    bit[ss] += 1
    while bit[ss] > 1:
        bit[ss + 1] += 1
        bit[ss] = bit[ss] & 1
        ss += 1
print(sum(bit))
