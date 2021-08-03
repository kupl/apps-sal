import math
t = int(input())


def glr(x):
    sigma_a = 0
    a = x
    sigma_n = (x * (x + 1)) // 2
    p = 0
    while(x > 0):

        if(x % 2 == 0):
            count = x // 2
        else:
            count = (x + 1) // 2

        sigma_a += count * (2**p)
        x -= count
        p += 1
    sigma_b = sigma_n - sigma_a

    sigma_b = sigma_b + (-1 * (int(math.log(a, 2))))

    return sigma_b


for i in range(t):

    l, r = list(map(int, input().split()))

    if(l > 1):
        ans = glr(r) - glr(l - 1)
    else:

        ans = glr(r) - 1

    print(ans)
