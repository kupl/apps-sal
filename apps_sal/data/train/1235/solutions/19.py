# cook your dish here
def power(x, y, p):

    res = 1  # Initialize result

    x = x % p  # Update x if it is more
    # than or equal to p

    while (y > 0):

        # If y is odd, multiply
        # x with result
        if (y & 1):
            res = (res * x) % p

        # y must be even now
        y = y >> 1  # y = y/2
        x = (x * x) % p

    return res

# function to calculate
# number of digits in x


def numberOfDigits(x):

    i = 0
    while (x):
        x //= 10
        i += 1

    return i

# function to print
# last 2 digits of 2^n


def LastTwoDigit(n):
    """print("Last " + str(2) + 
          " digits of " + str(2), end = "") 
    print("^" + str(n) + " = ", end = "")"""

    # Generating 10^2
    temp = 1
    for i in range(1, 3):
        temp *= 10

    # Calling modular exponentiation
    temp = power(5, n, temp)

    # Printing leftmost zeros.
    # Since (2^n)%2 can have digits
    # less then 2. In that case we
    # need to print zeros
    for i in range(2 - numberOfDigits(temp)):
        print(0, end="")

    # If temp is not zero then print temp
    # If temp is zero then already printed
    if temp:
        print(temp)

# Driver Code


def __starting_point():
    n = int(input())
    LastTwoDigit(n)


__starting_point()
