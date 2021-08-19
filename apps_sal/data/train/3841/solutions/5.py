def get_words(letter_counts):
    from itertools import permutations
    word = ''.join((count * char for (count, chars) in letter_counts.items() for char in chars))
    return sorted(set(map(lambda x: ''.join(x), permutations(word))))
