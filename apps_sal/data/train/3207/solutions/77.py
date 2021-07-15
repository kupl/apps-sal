def reverseWords(s):
    string = ''
    s = s.split()
    for word in reversed(range(len(s))):
        string += s[word]
        string += ' '
    string = string[:-1]
    return string
