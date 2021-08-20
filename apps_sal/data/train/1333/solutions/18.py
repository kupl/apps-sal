def solve(n, b):
    for i in range(n - 1):
        if b[i] & b[i + 1] != b[i]:
            print(0)
            return
    x = 0
    for i in range(n - 1):
        x += bin(b[i]).count('1')
    print(pow(2, x, mod))


mod = 10 ** 9 + 7
for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    solve(n, b)
