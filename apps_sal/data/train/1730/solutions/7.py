def two_by_n(n, k):
    op = [[k, 0], [k * (k - 1), k * (k - 1)]]
    for i in range(n - 2):
        op.append([op[-1][0] * (k - 1) + op[-1][1] * (k - 2), op[-2][0] * (k - 1) * (k - 2) + op[-2][1] * (k - 1 + (k - 2) * (k - 2))])
    return sum(op[n - 1]) % 12345787
