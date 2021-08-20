def word_pattern(pattern, string):
    words = string.split(' ')
    return len(pattern) == len(words) and len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words))
