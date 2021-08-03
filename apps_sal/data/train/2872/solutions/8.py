def coin(n):
    return gen_coin(n, "", [])


def gen_coin(n, solution, res):
    if n == 0:
        res.append(solution)
    else:
        gen_coin(n - 1, solution + "H", res)
        gen_coin(n - 1, solution + "T", res)
    return res
