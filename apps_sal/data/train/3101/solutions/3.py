from itertools import chain, permutations

def is_palindrome(w1, w2):
    return all(c1 == c2 for c1, c2 in zip(chain(w1, w2), chain(reversed(w2), reversed(w1))))

def palindrome_pairs(words):
    words = [str(word) for word in words]
    return [[i, j] for i, j in permutations(range(len(words)), 2) if is_palindrome(words[i], words[j])]
