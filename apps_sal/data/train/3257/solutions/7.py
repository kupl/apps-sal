from itertools import permutations


def slogan_maker(array):
    array = [e for index, e in enumerate(array) if array.index(e) == index]
    buzz_words = permutations(array, len(array))
    return [' '.join(buzz) for buzz in buzz_words]
