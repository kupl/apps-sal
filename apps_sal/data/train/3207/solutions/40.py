def reverseWords(s):
    w = s.split(' ')
    output = []
    for word in w:
        output.insert(0, word)
    return" ".join(output)
