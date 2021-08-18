T = int(input())
for i in range(T):
    arr = list(map(int, input().strip().split()))
    X = arr[0]
    Y = arr[1]

    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)

    def lcm(a, b):
        return (a / gcd(a, b)) * b

    num = lcm(X, Y)
    ans_X = num / X
    ans_Y = num / Y
    ans = int(ans_X + ans_Y - 2)
    print(ans)
