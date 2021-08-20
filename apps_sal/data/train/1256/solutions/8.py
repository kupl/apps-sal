for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    ans = ones = twos = 0
    for i in range(n):
        if A[i] == 1 or A[i] == 0:
            ones += 1
        elif A[i] == 2:
            twos += 1
    n = n - ones
    ct2 = 0
    if twos > 1:
        ct2 = twos
    ans = n * (n - 1) // 2 - ct2 * (ct2 - 1) // 2
    print(ans)
