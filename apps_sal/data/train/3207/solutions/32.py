def reverseWords(s):
    s = s.split()
    empty = []
    while len(s) > 0:
        empty.append(s.pop())
    else:
        return ' '.join(empty)
