# your code goes here.............
# Python 3 program to find sun of
# numbers formed by all permutations
# of given set of digits

# function to calculate factorial
# of a number
def factorial(n):

    f = 1
    if (n == 0 or n == 1):
        return 1
    for i in range(2, n + 1):
        f = f * i
    return f

# Function to calculate sum
# of all numbers


def getSum(arr, n):

    # calculate factorial
    fact = factorial(n)

    # sum of all the given digits at
    # different positions is same and
    # is going to be stored in digitsum.
    digitsum = 0
    for i in range(n):
        digitsum += arr[i]
    digitsum *= (fact // n)

    # Compute result (sum of
    # all the numbers)
    res = 0
    i = 1
    k = 1
    while i <= n:
        res += (k * digitsum)
        k = k * 10
        i += 1

    return res

# Driver Code


def __starting_point():

    # n distinct digits
    t = int(input())
    for _ in range(t):
        m = int(input())
        arr = list(map(int, input().split()))
        n = len(arr)

    # Print sum of all the numbers formed
        print(getSum(arr, n))

# This code is contributed by ita_c


__starting_point()
