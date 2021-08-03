from random import randint

f = input

# f = open("in.txt", "r").readline


def din(st):
    return bin(st)[2:].zfill(10)


def func(x, y, n):
    # count = 0
    # for z in range(0, n+1):
    #     print(din(x), "xor", din(z), end=" ")
    #     if x ^ z < y ^ z:
    #         count += 1
    #         print("<", end=" ")
    #     else:
    #         print(">=", end="")
    #     print(din(y), "xor", din(z), "z =", z)
    z0 = x ^ 0 < y ^ 0
    unmatch = 1
    # print(z0)
    # print(x ^ unmatch < y ^ unmatch)
    while z0 == (x ^ unmatch < y ^ unmatch) and unmatch < n + 1:
        # print(unmatch < n+1)
        unmatch *= 2
        # print("unmatch =", unmatch)
    # print("x y =", x, y)
    # print("unmatch =", unmatch)
    # print("n =", n)
    ans = ((n + 1) // (unmatch * 2)) * unmatch
    ans += min(unmatch, (n + 1) - (ans * 2))
    # print("ans =", ans)
    return (ans if z0 else ((n + 1) - ans))


for _ in range(int(f())):
    x, y, n = list(map(int, f().split()))
    # x, y = (randint(1, 20), randint(1, 20))
    print(func(x, y, n))
