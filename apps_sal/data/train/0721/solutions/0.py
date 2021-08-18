def permutation(n, p):
    r = 26
    if n == 1:
        return 26
    elif n == 2:
        return 52
    elif n == 3:
        return 728
    else:
        if n % 2 == 0:
            return ((2 * (bin_expo(r, ((n // 2) + 1), p) - r) * bin_expo(25, 1000000005, p))) % p
        else:
            n = n + 1
            return ((2 * ((bin_expo(r, (n // 2 + 1), p) - r) * bin_expo(r - 1, 1000000005, p))) - bin_expo(26, n // 2, p)) % p


def bin_expo(x, n, p):
    if n == 0:
        return 1
    elif n == 1:
        return x % p
    else:
        temp = bin_expo(x, n // 2, p)
        temp = (temp * temp) % p
        if n % 2 == 0:
            return temp
        else:
            return ((x % p) * temp) % p


test = int(input())
for _ in range(test):
    n = int(input())
    p = 1000000007
    print(int(permutation(n, p)))
