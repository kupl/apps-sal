for _ in range(int(input())):
    n = int(input())
    z = 0
    for _ in range(n):
        z += input().strip().split(' ').count('0')

    k = 2
    r = n - 1
    cs = k
    while cs <= z:
        r -= 1
        k += 2
        cs += k
    print(r)
