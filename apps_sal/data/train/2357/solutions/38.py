from numba import njit
N, M, *A = [int(_) for _ in open(0).read().split()]
mod = 10**9 + 7
suma = sum(A)
x = M + N
y = N + suma
a = 1
b = 1


@njit('i8(i8,i8,i8)')
def pow_mod(base, exp, mod):
    exp %= mod - 1
    res = 1
    while exp:
        if exp & 1:
            res = res * base % mod
        base = base * base % mod
        exp >>= 1
    return res


@njit('i8(i8,i8)')
def comb(x, y):
    a = b = 1
    for _ in range(y):
        a *= x
        b *= y
        a %= mod
        b %= mod
        x -= 1
        y -= 1
    ret = a * pow_mod(b, mod - 2, mod) % mod
    return ret


print((comb(M + N, N + suma)))
