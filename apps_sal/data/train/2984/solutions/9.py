def infected_zeroes(lst):
    one = "".join(str(d) for d in lst).split("0")
    return max(len(one[0]), len(one[-1]), *((len(o) + 1) // 2 for o in one[1:-1]))
