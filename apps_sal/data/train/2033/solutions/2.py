n = int(input())
arr = list(map(int, input().split()))
b, c = [0], [0]
curr = 1
for i in range(1, n + 1):
    b.extend([curr] * arr[i])
    curr += arr[i]
curr = 1
for i in range(1, n + 1):
    if arr[i] > 1 and arr[i - 1] > 1:
        c.append(curr - 1)
        c.extend([curr] * (arr[i] - 1))
    else:
        c.extend([curr] * arr[i])
    curr += arr[i]
if b == c:
    print('perfect')
else:
    print('ambiguous')
    print(*b)
    print(*c)
