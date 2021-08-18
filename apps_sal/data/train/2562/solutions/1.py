from itertools import groupby


def __starting_point():

    for el, el_list in groupby(input()):
        print((len(list(el_list)), int(el)), end=' ')


__starting_point()
