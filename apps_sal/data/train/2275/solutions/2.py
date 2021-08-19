import sys
input = sys.stdin.readline
mod = 1000000007

t = int(input())
for tests in range(t):
    n, p = list(map(int, input().split()))
    K = sorted(map(int, input().split()), reverse=True)

    if p == 1:
        if n % 2 == 0:
            print(0)
        else:
            print(1)
        continue

    ANS = [0, 0]
    flag = 0

    for i in range(n):
        k = K[i]

        if ANS[0] == 0:
            ANS = [1, k]

        elif ANS[1] == k:
            ANS[0] -= 1

        else:
            while ANS[1] > k:
                ANS[0] *= p
                ANS[1] -= 1

                if ANS[0] > 10**7:
                    flag = 1
                    lastind = i
                    break

            if flag == 1:
                A = ANS[0] * pow(p, ANS[1], mod) % mod
                # print(A,ANS)

                for j in range(lastind, n):
                    A = (A - pow(p, K[j], mod)) % mod
                print(A)
                break
            else:
                ANS[0] -= 1

    if flag == 0:
        print(ANS[0] * pow(p, ANS[1], mod) % mod)
