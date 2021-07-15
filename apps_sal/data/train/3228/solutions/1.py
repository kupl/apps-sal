def word_pattern(pattern, string):
    return [pattern.index(any) for any in pattern] == [string.split().index(any) for any in string.split()]
