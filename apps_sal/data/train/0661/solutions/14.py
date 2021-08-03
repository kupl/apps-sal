import math
t, n = input().split()
t = int(t)
n = int(n)

for _ in range(t):
    num = eval(input())
    num = int(num)
    # print("num",num)
    sq = int(math.sqrt(num))
    # print("sq",sq)
    squ = int(sq**2)
    # print("squ",squ)
    diff = 0.01 * n * num
    # print("diff",diff)

    if (num - squ) <= diff:
        print("yes")
    else:
        print("no")
