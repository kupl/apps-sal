import numpy as np
t = int(input())
while(t):
    t -= 1
    n, m, k = [int(x) for x in list(input().split())]
    l = np.array([["."] * m] * n)
    while(k):
        k -= 1
        x, y = [int(x) for x in list(input().split())]
        l[x - 1][y - 1] = "X"
    sum = 0
    for i in range(n):
        for j in range(m):
            if(l[i][j] == "X"):
                if(i == 0 or l[i - 1][j] == "."):
                    sum += 1
                if(i == n - 1 or l[i + 1][j] == "."):
                    sum += 1
                if(j == 0 or l[i][j - 1] == "."):
                    sum += 1
                if(j == m - 1 or l[i][j + 1] == "."):
                    sum += 1
    print(sum)
