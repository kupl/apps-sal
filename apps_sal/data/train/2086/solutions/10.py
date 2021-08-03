from collections import deque
n, m = list(map(int, input().split()))
arr = deque(list(map(int, input().split())))

max_v = max(arr)

ans = []
while arr[0] != max_v:
    a = arr.popleft()
    b = arr.popleft()
    if a > b:
        arr.appendleft(a)
        arr.append(b)
    else:
        arr.appendleft(b)
        arr.append(a)
    ans.append((a, b))

for i in range(m):
    q = int(input())
    q -= 1
    if q < len(ans):
        print(*ans[q])
    else:
        print(arr[0], arr[(q - len(ans)) % (len(arr) - 1) + 1])
