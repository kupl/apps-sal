def reverseWords(s):
    words = s.split()
    words = list(reversed(words))
    return ' '.join(words)
