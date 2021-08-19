from itertools import product


def __starting_point():
    arr1 = list(map(int, input().strip().split(' ')))
    arr2 = list(map(int, input().strip().split(' ')))
    for el in product(arr1, arr2):
        print('{} '.format(el), end='')


__starting_point()
