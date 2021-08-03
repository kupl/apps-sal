is_vowel = set("aeiouyAEIOUY").__contains__


def vowel_indices(word):
    return [i for i, c in enumerate(word, 1) if is_vowel(c)]
