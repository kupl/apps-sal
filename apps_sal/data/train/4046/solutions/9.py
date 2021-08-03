from functools import reduce


def calculate_scrap(scraps, number_of_robots):
    ans = reduce(lambda x, y: x / (100 - y) * 100, scraps, number_of_robots * 50)
    return int(ans) if ans.is_integer() else int(ans) + 1
