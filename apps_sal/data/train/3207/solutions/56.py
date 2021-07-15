def reverseWords(s):
    word = list(s.split(' '))
    word.reverse()
    return ' '.join(word)
