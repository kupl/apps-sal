# from functools import reduce


def am_i_wilson(n):

    # print(((reduce(lambda a, b: a * b, list(range(1, n))) + 1) %
    #      (n ** 2)) == 0 if n > 2 else False)

    # This is the only way to do this kata, else it will say Timeout error LoL

    return(n in [5, 13, 563])
