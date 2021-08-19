import math
for _ in range(int(input())):
    n = int(input())

    def findNumber(n):
        x = int(math.ceil((-1 + math.sqrt(1 + 8 * n + 8)) / 2))
        x -= 1
        b = x * (x + 1) // 2 - 1
        res = n - b - 1
        return res
    ans = findNumber(n)
    print(ans)
