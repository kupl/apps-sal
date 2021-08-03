def xnor(a, b):
    if (a < b):
        a, b = b, a

    if (a == 0 and b == 0):
        return 1

    a_rem = 0
    b_rem = 0

    count = 0

    xnornum = 0

    while (a):
        a_rem = a & 1

        b_rem = b & 1
        if (a_rem == b_rem):
            xnornum |= (1 << count)

        count += 1
        a = a >> 1
        b = b >> 1
    return xnornum


def xor(a, b, n):
    if((n + 2) % 3 == 0):
        return a
    elif((n + 1) % 3 == 0):
        return b
    else:
        return a ^ b


def check(a, b, n):
    if(n == 1):
        return a
    elif(n == 2):
        return b
    if(n <= 6):
        ans = xnor(a, b)
        for i in range(3, n):
            ans, b = xnor(ans, b), ans
        return ans
    elif((n - 4) % 3 == 0):
        return a
    elif((n - 5) % 3 == 0):
        return b
    elif((n - 6) % 3 == 0):
        return xnor(a, b)


for z in range(int(input())):
    a, b, n = map(int, input().split())
    print(max(xor(a, b, n), check(a, b, n)))
