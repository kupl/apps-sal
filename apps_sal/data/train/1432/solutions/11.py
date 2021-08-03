# cook your dish here
T = int(input())
for i in range(T):
    n = int(input())
    A = []
    for i in range(0, n):
        A.append([int(i) for i in input().split()])
    ones = sum([sum(i) for i in A])
    compare = n
    ans = 0
    for i in range(0, n):
        if ones <= compare:
            ans = i
            break
        compare += 2 * (n - 1 - i)
    print(ans)
