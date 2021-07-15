def solve(n,k):
    arr = list(range(n))
    for i in range(n):
        arr = arr[:i]+arr[i:][::-1]
    return arr.index(k)
