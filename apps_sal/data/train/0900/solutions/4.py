from sys import stdin, stdout


def power(x, y, p):

    res = 1  # Initialize result

    # Update x if it is

    # more than or equal to p

    x = x % p

    while (y > 0):

        # If y is odd, multiply

        # x with the result

        if (y & 1):

            res = (res * x) % p

        # y must be even now

        y = y >> 1  # y = y/2

        x = (x * x) % p

    return res


def sin():
    return stdin.readline()


def out(s):
    stdout.write(str(s) + "\n")


m = 1000000007
for i in range(int(input())):
    n = sin()[:-1]
    remainderB = 0
    for i in range(len(n)):
        remainderB = ((remainderB * 10

                       + ord(n[i]) - 48) %

                      (m - 1));
    out((power(2, remainderB, m) * 5) % m)
