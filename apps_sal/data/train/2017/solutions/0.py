n = int(input())

xs = [int(x) for x in input().split()]

seen = {}

res = 0

while xs:
    j = xs.index(xs[0], 1)
    res += j - 1
    xs = xs[1:j] + xs[j + 1:]

print(res)
