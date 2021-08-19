from itertools import permutations


def get_words(hash_of_letters):
    letters = ''.join((cnt * c for (cnt, cs) in hash_of_letters.items() for c in cs))
    return sorted({''.join(xs) for xs in permutations(letters)})
