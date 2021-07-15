# https://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/


def zfunc(string):
    if not string:
        return []

    strlen = len(string)
    Z = [0] * strlen

    # [L,R] make a window which matches with prefix of s
    L = R = 0
    for i in range(1, strlen):
        # if i>R nothing matches so we will calculate.
        # Z[i] using naive way.
        if i > R:
            L = R = i

            # R-L = 0 in starting, so it will start
            # checking from 0'th index. For example,
            # for "ababab" and i = 1, the value of R
            # remains 0 and Z[i] becomes 0. For string
            # "aaaaaa" and i = 1, Z[i] and R become 5
            while R < strlen and string[R - L] == string[R]:
                R += 1
            Z[i] = R - L
            R -= 1
        else:
            # k = i-L so k corresponds to number which
            # matches in [L,R] interval.
            k = i - L
            # if Z[k] is less than remaining interval
            # then Z[i] will be equal to Z[k].
            # For example, str = "ababab", i = 3, R = 5
            # and L = 2
            if Z[k] < R - i + 1:
                # For example str = "aaaaaa" and i = 2, R is 5,
                # L is 0
                Z[i] = Z[k]
            else:
                # else start from R and check manually
                L = i
                while R < strlen and string[R - L] == string[R]:
                    R += 1
                Z[i] = R - L
                R -= 1
    Z[0] = strlen
    return Z

