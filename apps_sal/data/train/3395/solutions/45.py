def remove_duplicate_words(s):
    s = s.split(' ')
    a = ''
    for x in range(len(s)):
        if s[x] not in a:
            a += s[x] + ' '
    return a[:-1]
