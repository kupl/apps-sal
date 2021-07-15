def remove_duplicate_words(s):
    d = dict((i,s.split(' ').count(i)) for i in s.split(' '))
    return ' '.join(d.keys())
