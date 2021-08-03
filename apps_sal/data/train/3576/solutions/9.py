def longest(words):
    lon = len(words[0])
    for i in words:
        if len(i) > lon:
            lon = len(i)
    return lon
