import math


def __starting_point():
    for _ in range(int(input())):
        n = int(input())
        a = list(set(map(int, input().split())))
        n = len(a)
        flag = 0
        if n == 1:
            print(a[0] * 2)
        else:
            Lgcd = [0]
            Rgcd = [0]
            for i in range(n):
                gcd = math.gcd(Lgcd[i], a[i])
                Lgcd.append(gcd)
            a = a[::-1]
            for i in range(n):
                gcd = math.gcd(Rgcd[i], a[i])
                Rgcd.append(gcd)
            Rgcd = Rgcd[::-1]

            a = a[::-1]
            ans = []
            for i in range(n):
                gcd = a[i] + math.gcd(Lgcd[i], Rgcd[i + 1])
                ans.append(gcd)
            print(max(ans))


__starting_point()
