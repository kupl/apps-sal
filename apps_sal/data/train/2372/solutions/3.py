from sys import stdin

tt = int(stdin.readline())

for loop in range(tt):

    n = int(stdin.readline())

    x = int(n**0.5)
    ans = float("inf")

    for i in range(x - 10, x + 10):

        for j in range(x - 10, x + 10):

            if i > 0 and j > 0 and i * j >= n:
                ans = min(ans, i + j - 2)

    print(ans)
