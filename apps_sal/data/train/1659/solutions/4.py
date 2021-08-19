dictionary = {}


def exp_sum(n, k=None):
    if k is None or k > n:
        k = n
    # use the usual recurrence relation, and memoization
    if n == 0 and k == 0:
        return 1
    elif n < 0 or k < 0:
        return 0
    else:
        if (n, k) in dictionary:
            return dictionary[(n, k)]
        else:
            sigma = 0
            for m in range(1, k + 1):
                sigma += exp_sum(n - m, m)
            dictionary[(n, k)] = sigma
            return sigma
