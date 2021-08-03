from math import gcd


def game(cPose, cGCD):
    if cPose == n:
        return 1 if cGCD == 1 else 0

    if (cPose, cGCD) in dp:
        return dp[(cPose, cGCD)]

    dp[(cPose, cGCD)] = game(cPose + 1, cGCD) + game(cPose + 1, gcd(cGCD, l[cPose]))
    return dp[(cPose, cGCD)]


for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    dp = {}
    ans = 0
    for i in range(n):
        ans += game(i + 1, l[i])
    print(ans)
