t = int(input())
for x in range(t):
    a, b, n = list(map(int, input().split()))
    import math

    def togglebit(n):

        if (n == 0):
            return 1

        i = n

        n = n | (n >> 1)

        n |= n >> 2
        n |= n >> 4
        n |= n >> 8
        n |= n >> 16

        return i ^ n

    def xnor(num1, num2):

        if (num1 < num2):
            temp = num1
            num1 = num2
            num2 = temp
        num1 = togglebit(num1)

        return num1 ^ num2

    def xor(x, y, p):
        if p % 3 == 1:
            return x
        elif p % 3 == 2:
            return y
        elif p % 3 == 0:
            return (x ^ y)

    def xnnor(x, y, p):
        if p % 3 == 1:
            return x
        elif p % 3 == 2:
            return y
        elif p % 3 == 0:
            return xnor(x, y)
    print(max(xor(a, b, n), xnnor(a, b, n)))
