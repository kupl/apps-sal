def reverseWords(str):
    s = str.split(' ')
    string = []
    for e in s:
        string.insert(0, e)
    return ' '.join(string)
