import sys
from collections import deque
n = int(input())
if n % 4 == 2 or n % 4 == 3:
    print('-1')
    return

arr = [None] * (n + 1)
qt = deque([i for i in range(1, n + 1)])
mark = set()
while qt:
    while qt and qt[0] in mark:
        qt.popleft()
    if not qt:
        break
    a = qt.popleft()
    while qt and qt[0] in mark:
        qt.popleft()
    if not qt:
        break
    b = qt.popleft()
    for i in range(4):
        mark.add(a)
        mark.add(b)
        arr[a] = b
        arr[b] = n - a + 1
        a = b
        b = arr[b]

for i in range(1, n + 1):
    if not arr[i]:
        arr[i] = a
        break
print(' '.join(map(str, arr[1:])))
