def reverseWords(s):
    words = s.split()
    i = ''
    index = len(words)
    while index > 0:
        index -= 1
        i = i+ ' ' + (words[index])
    return i[1:]
