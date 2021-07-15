def longest(words):
    sorted_list = sorted(words, key=len, reverse=True)
    return len(sorted_list[0])
