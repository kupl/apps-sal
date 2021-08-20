t = int(input())


def xnor(a, b):
    if a < b:
        (a, b) = (b, a)
    if a == 0 and b == 0:
        return 1
    a_rem = 0
    b_rem = 0
    count = 0
    xnornum = 0
    while a != 0:
        a_rem = a & 1
        b_rem = b & 1
        if a_rem == b_rem:
            xnornum |= 1 << count
        count = count + 1
        a = a >> 1
        b = b >> 1
    return xnornum


while t:
    t -= 1
    (a, b, n) = input().split()
    (a, b, n) = (int(a), int(b), int(n))
    if n % 3 == 1:
        print(a)
        continue
    if n % 3 == 2:
        print(b)
        continue
    xor_ = a ^ b
    xnor_ = xnor(a, b)
    print(max(xor_, xnor_))
