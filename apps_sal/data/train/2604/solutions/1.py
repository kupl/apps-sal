from itertools import permutations


def __starting_point():
    in_data = list(input().strip().split(' '))
    for el in permutations(sorted(in_data[0]), int(in_data[1])):
        print(''.join(el))


__starting_point()
