from itertools import groupby


def __starting_point():
    #in_data = input().strip().split(' ')

    for el, el_list in groupby(input()):
        print((len(list(el_list)), int(el)), end=' ')


__starting_point()
