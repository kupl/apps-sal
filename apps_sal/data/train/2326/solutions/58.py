from bisect import bisect_left, bisect_right

N = int(input())
As = list(map(int, input().split()))

Bs = [0]
xs = [-1]
for i, A in enumerate(As):
    if Bs[-1] < A:
        Bs.append(A)
        xs.append(i)

lenB = len(Bs)
sumAs = [0] * lenB
numFulls = [0] * lenB
for A in As:
    i = bisect_left(Bs, A)
    sumAs[i] += A - Bs[i - 1]
    numFulls[i - 1] += 1

for i in reversed(list(range(lenB - 1))):
    numFulls[i] += numFulls[i + 1]

anss = [0] * N
for i in range(1, lenB):
    ans = sumAs[i]
    ans += (Bs[i] - Bs[i - 1]) * numFulls[i]
    anss[xs[i]] = ans

print(('\n'.join(map(str, anss))))
