import itertools


def is_palindrome(word):
    return word == word[::-1]


def palindrome_pairs(words):
    words = list(map(str, words))
    return [[i, j] for (i, j) in itertools.permutations(range(len(words)), 2) if is_palindrome(words[i] + words[j])]
