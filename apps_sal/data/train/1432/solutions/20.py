from sys import stdin

T = int(stdin.readline())

for i in range(0, T):
    n = int(stdin.readline())
    A = []
    for i in range(0, n):
        A.append([int(i) for i in stdin.readline().split(' ')])
    ones = sum([sum(i) for i in A])
    compare = n
    ans = 0
    for i in range(0, n):
        if ones <= compare:
            ans = i
            break
        compare += 2 * (n - 1 - i)
    print(ans)
