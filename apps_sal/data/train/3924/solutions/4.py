def reverse_words(str):
    return " ".join(map(lambda word: word[::-1], str.split(' ')))
