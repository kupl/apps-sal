# cook your dish here
import math


def findX(list, int):
    # Sort the given array
    list.sort()

    # Get the possible X
    x = list[0] * list[int - 1]

    # Container to store divisors
    vec = []

    # Find the divisors of x
    i = 2
    while(i * i <= x):
        # Check if divisor
        if(x % i == 0):
            vec.append(i)
            if ((x // i) != i):
                vec.append(x // i)
        i += 1

    # sort the vec because a is sorted
        # and we have to compare all the elements
    vec.sort()
    # if size of both vectors is not same
    # then we are sure that both vectors
    # can't be equal
    if(len(vec) != int):
        return -1
    else:
        # Check if a and vec have
        # same elements in them
        j = 0
        for it in range(int):
            if(list[j] != vec[it]):
                return -1
            else:
                j += 1
    return x


# Driver code
try:

    m = int(input())
    for i in range(m):
        n = int(input())
        x = list(map(int, input().split()))

        print(findX(x, n))
except EOFError as e:
    print(e)
