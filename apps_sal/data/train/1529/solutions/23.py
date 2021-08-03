import math


def fun():
    T = int(input())
    ans = []
    for i in range(T):
        T = int(input())
        l = list(input().split())
        l = [int(x) for x in l]
        x = []
        for j in range(len(l)):
            x += [math.factorial(len(l) - 1) * k * math.pow(10, j) for k in l]
            # print(x)
        x1 = [int(j) for j in x]
        x = sum(x1)
        # print(x)
        ans.append(x)

    for j in ans:
        print(j)


fun()
