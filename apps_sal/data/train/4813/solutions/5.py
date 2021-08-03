holes = {"0": 1, "6": 1, "8": 2, "9": 1}


def get_num(n):
    return sum(holes.get(i, 0) for i in str(n))
