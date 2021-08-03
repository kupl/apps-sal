def reverseWords(s):
    words = s.split()
    return ' '.join([words[-i - 1] for i in range(len(words))])
