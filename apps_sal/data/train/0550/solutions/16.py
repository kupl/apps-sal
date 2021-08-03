import math
t = int(input())
for ti in range(t):
    a, b = map(int, input().split())
    mx = max(a, b)
    bit = int((math.log(mx) / math.log(2)) + 1)
    num = pow(2, bit) - 1
    res = a ^ b
    cnt = 0
    rot = 0
    for i in range(1, bit):
        if b % 2 == 0:
            b //= 2
        else:
            b += num
            b //= 2
        ans = a ^ b
        cnt += 1
        if ans > res:
            res = ans
            rot = cnt
    print(str(rot) + " " + str(res))
