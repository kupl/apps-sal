for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    d1, d2 = [0], [0]
    s1 = s2 = ans = 0
    for i in range(N):
        s1 += A[i]
        s2 += B[i]
        d1.append(s1 * (i + 1))
        d2.append(s2 * (i + 1))
    #  print(d1, d2)
    for i in range(N):
        if (d1[i] == d2[i]) and (d1[i + 1] == d2[i + 1]):
            ans += A[i]
    print(ans)
