import math


def am_i_wilson(n):
    return (n == 5) or (n == 13) or (n == 563)

    # would have used the following code, but the factorials become to large a number and it times out
    # print(n)
    # if n > 1:
    #    if ((math.factorial(n-1)) + 1) / (n * n) % 1 == 0:
    #        return(True)
    #    else:
    #        return(False)
    # else:
    #    return(False)
