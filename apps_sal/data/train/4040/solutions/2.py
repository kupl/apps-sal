def nth_char(words):
    result = ''
    for (index, word) in enumerate(words):
        result += word[index]
    return result
