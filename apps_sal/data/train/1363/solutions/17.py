
import sys

f = sys.stdin

if len(sys.argv) > 1:
    f = open(sys.argv[1], "rt")

T = int(f.readline().strip())

MOD = 10**9 + 7


def calc(N, D):
    X = [D] * N

    X_d = [0] * N  # X * D
    carry = 0
    for i in range(N):
        val = D * D + carry
        X_d[i] = val % 10
        carry = val // 10
    assert carry < 10
    X_d.append(carry)  # Could be 0, still use for convenience.

    product = [0] * (2 * N)
    #~ print(X_d)
    #~ print(product)

    # (1)
    carry = 0
    cur_sum = 0
    for i in range(N):
        cur_sum += X_d[i]
        val = cur_sum + carry
        product[i] = val % 10
        carry = val // 10

    # (2)
    cur_sum += X_d[N]
    for i in range(N):
        cur_sum -= X_d[i]
        val = cur_sum + carry
        product[N + i] = val % 10
        carry = val // 10

    # (3)
    while carry > 0:
        product.append(carry % 10)
        carry = carry // 10

    while product and product[-1] == 0:
        del product[-1]

    h = 0
    for x in product:
        h = (h * 23 + x) % MOD

    return h


for case_id in range(1, T + 1):
    N, D = list(map(int, f.readline().strip().split()))

    r = calc(N, D)

    print(r)
