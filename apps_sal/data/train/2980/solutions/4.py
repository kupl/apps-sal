def count_divs(n):
    is_square = 0
    if n**0.5 % 1 == 0:
        is_square = 1
    return len([(x, n / x) for x in range(1, int(n**0.5) + 1) if n % x == 0]) * 2 - is_square


min_num = {count_divs(i): i for i in reversed(range(1, 10**5))}


def find_min_num(num_div):
    return min_num[num_div]
