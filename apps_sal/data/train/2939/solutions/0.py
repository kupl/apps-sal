def has_two_cube_sums(n):
    cubic_list = [i**3 for i in range(1, int((n)**(1. / 3.)) + 1)]
    return sum([(n != 2 * c) and ((n - c) in cubic_list) for c in cubic_list]) > 3
