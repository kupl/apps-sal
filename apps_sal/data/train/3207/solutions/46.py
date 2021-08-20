def reverseWords(s):
    return ' '.join((w[::-1] for w in s.split()))[::-1]
