

# Python3 code for calculating
# the number of squares

# Recursive function to
# return gcd of a and b
def __gcd(a, b):
    # Everything divides 0
    if (a == 0 or b == 0):
        return 0

        # base case
    if (a == b):
        return a

        # a is greater
    if (a > b):
        return __gcd(a - b, b)
    return __gcd(a, b - a)


# Function to find
# number of squares
def NumberOfSquares(x, y):
    # Here in built PHP
    # gcd function is used
    s = __gcd(x, y)

    ans = (x * y) / (s * s)

    return int(ans)


# Driver Code

t = int(input())
for i in range(t):
    m, n = list(map(int, input().split(' ')))
# Call the function
# NumberOfSquares
    print((NumberOfSquares(m, n)))

# This code is contributed
# by mit
