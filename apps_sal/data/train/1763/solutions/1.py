MOD = 12345787


def n_choose_k(n, k):
    if not k or n == k:
        return 1
    if k < 0 or k > n:
        return 0
    if 2 * k > n:
        k = n - k
    ans = 1
    for i in range(k):
        ans = (ans * (n - i) // (i + 1))
    return ans


def insane_inc_or_dec(x):
    return (n_choose_k(9 + x, x) + n_choose_k(10 + x, x) - 10 * x - 2) % MOD
