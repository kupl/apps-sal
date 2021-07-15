def reverseWords(s):
    ls = s.split()
    lsn = ls[::-1]
    return ' '.join(lsn)
