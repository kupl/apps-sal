def reverseWords(s):
    s = s.split(' ')
    string = []
    for w in s:
        string.insert(0, w)
    string = ' '.join(string)
    return string[:]

