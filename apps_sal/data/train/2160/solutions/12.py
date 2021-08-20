(n, k) = input().split()
(n, k) = (int(n), int(k))
V = [int(s) for s in input().split()]
sumV = sum(V)
S = []
count = 0
currentLength = 0
possible = sumV % k == 0
target = sumV // k
for v in V:
    count += 1
    currentLength += v
    if currentLength == target:
        S.append(count)
        count = 0
        currentLength = 0
    elif currentLength > target:
        possible = False
        break
if possible:
    print('Yes')
    for s in S:
        print(s, end=' ')
else:
    print('No')
