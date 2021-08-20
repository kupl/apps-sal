n = int(input())
health = list(map(int, input().split()))
initial = int(input())
if n > 1:
    health.sort()
points = 0
mxpts = 0
(i, j) = (0, n - 1)
while i < j and i < n and (j >= 0):
    if health[i] <= initial:
        points += 1
        mxpts = max(points, mxpts)
        initial -= health[i]
        i += 1
    elif points > 0:
        initial += health[j]
        j -= 1
        points -= 1
    else:
        break
print(mxpts)
