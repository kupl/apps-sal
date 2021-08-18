OPTIONS = [1, 5, 10, 50]


def solve(n):
    print(n)
    base_answer = len(rec_solve(min(n, 11)))

    if n < 12:
        return base_answer
    else:
        return base_answer + (49 * (n - 11))


def rec_solve(n, options=4, val=0):
    if n == 1:
        return_set = set()
        for i in range(1, options + 1):
            return_set.add(val + OPTIONS[-i])
        return return_set

    elif options == 1:
        return {val + 50 * n}

    return_set = set()
    for option_num in range(options, 0, -1):
        return_set = return_set.union(rec_solve(n - 1, option_num,
                                                val + OPTIONS[-option_num]))
    return return_set
