from itertools import starmap


def disarium_number(number):
    return ('Not !!', 'Disarium !!')[number == sum(starmap(pow, [(x, i + 1) for (i, x) in enumerate(map(int, str(number)))]))]
