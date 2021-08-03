def is_palindrome(word):
    return word == word[::-1]


def palindrome_pairs(words):
    words = [str(word) for word in words]
    return [
        [i, j]
        for i, word_i in enumerate(words)
        for j, word_j in enumerate(words)
        if i != j and is_palindrome(word_i + word_j)
    ]
