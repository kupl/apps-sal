t = int(input())
for x in range(t):
    a, b, n = list(map(int, input().split()))
    import math

# Please refer below post for details of this function
# https://www.geeksforgeeks.org/toggle-bits-significant-bit/
    def togglebit(n):

        if (n == 0):
            return 1

        # Make a copy of n as we are
        # going to change it.
        i = n

        # Below steps set bits after
        # MSB (including MSB)

        # Suppose n is 273 (binary
        # is 100010001). It does following
        # 100010001 | 010001000 = 110011001
        n = n | (n >> 1)

        # This makes sure 4 bits
        # (From MSB and including MSB)
        # are set. It does following
        # 110011001 | 001100110 = 111111111
        n |= n >> 2
        n |= n >> 4
        n |= n >> 8
        n |= n >> 16

        return i ^ n

    # Returns XNOR of num1 and num2
    def xnor(num1, num2):

        # Make sure num1 is larger
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
    # print(xor(a,b,n),xnor(a,b,n))
    print(max(xor(a, b, n), xnnor(a, b, n)))
