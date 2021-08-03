from itertools import permutations


def remove_duplicates(list):
    unique = []
    for l in list:
        if l not in unique:
            unique.append(l)
    return unique


def slogan_maker(input):
    input = remove_duplicates(input)
    output = []
    for p in permutations(input, len(input)):
        output.append(' '.join(p))
    return output
