def sort_it(s, n):
    words = s.split(', ')
    return ', '.join(word for word in sorted(words, key=lambda x: x[n - 1]))
