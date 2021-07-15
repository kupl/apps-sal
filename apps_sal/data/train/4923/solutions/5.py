def count_feelings(s, arr):
    count = sum([all([char in s and s.count(char) >= f.count(char) for char in f]) for f in arr])
    return '{count} {tense}.'.format(count=count, tense='feeling' if count == 1 else 'feelings')
