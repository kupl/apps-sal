import math


def hcf(a, b):
    if a == 0:
        return 1
    if a % b == 0:
        return b
    return hcf(b, a % b)


t = int(input())
for _ in range(t):
    n = int(input())
    list1 = list(map(int, input().strip().split()))

    curr = list1[0]
    for i in range(1, n):
        curr = hcf(curr, list1[i])
        if curr == 1:
            break

    if curr == 1:
        print(-1)
    else:
        ans = -1
        for i in range(2, math.floor(math.sqrt(curr)) + 1):
            if curr % i == 0:
                ans = i
                break

        if ans == -1:
            print(curr)
        else:
            print(i)
