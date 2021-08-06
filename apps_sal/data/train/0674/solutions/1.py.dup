import numpy as np
for _ in range(int(input())):
    ans = np.float('inf')
    n, m = (int(x) for x in input().split())
    sig = np.zeros((n, m))
    img = np.zeros((3 * n, 3 * m))
    for row in range(n):
        sig[row, :] = np.array([int(x) for x in input()])
    for row in range(n):
        img[row + n, m:2 * m] = np.array([int(x) for x in input()])
    for i in range(2 * n):
        for j in range(2 * m):
            ans = min(ans, np.abs(np.sum(img[i:n + i, j:m + j] != sig)))
    print(ans)
