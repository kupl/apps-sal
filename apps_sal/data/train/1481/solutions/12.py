

def solve(b, n):
    x = 0
    y = 0
    for i in range(n):
        if b[i] == '1':
            x += 1
        else:
            y += 1
    if x == n or y == n:
        return -1

    return abs(x - y) // 2


for tests in range(int(input())):
    b = input()
    n = len(b)
    if n % 2 == 1:
        print(-1)
    else:
        print(solve(b, n))
