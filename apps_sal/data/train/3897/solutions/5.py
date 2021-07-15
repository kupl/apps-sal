def solve(n,k):
    arr = []
    for i in range(n%2 + n//2):
        arr += [n - i - 1] + [i]
    return arr.index(k)
