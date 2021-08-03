from itertools import permutations


def get_words(letters):
    word = "".join(qty * char for qty in letters for chars in letters[qty] for char in chars)
    return sorted({"".join(permutation) for permutation in permutations(word)})
