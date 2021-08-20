from itertools import combinations


def __starting_point():
    in_data = list(input().strip().split(' '))
    for lng in range(1, int(in_data[1]) + 1):
        for el in combinations(sorted(in_data[0]), lng):
            print(''.join(el))


__starting_point()
