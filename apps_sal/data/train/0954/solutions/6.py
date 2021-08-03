def solve(n):
    s = 0
    for i in range(1, n):
        s += 2 * i * i * i
    s += n * n * n
    return s


for _ in range(int(input())):
    n = int(input())
    print(solve(n))
