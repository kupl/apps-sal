def read_data():
    n, k = map(int, input().split())
    As = []
    m = 0
    for i in range(k):
        ma = list(map(int, input().split()))
        As.append(ma[1:])
        m += ma[0] - 1
    return n, k, As, m

def solve(n, k, As, m):
    As.sort()
    steps = n + 1 + m
    mat1 = As[0]
    for i, mi in enumerate(mat1, 1):
        if i == mi:
            steps -= 2
        else:
            break
    return steps

n, k, As, m = read_data()
print(solve(n, k, As, m))
