def reverseWords(s):
    print(s)
    words = s.split()
    rev = ''
    i = len(words)
    while i > 0:
        i -= 1
        rev += words[i] + ' '
    print(rev)
    return rev[:-1]
