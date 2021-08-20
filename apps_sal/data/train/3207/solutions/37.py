def reverseWords(s):
    holder = s.split(' ')
    (i, j) = (0, len(holder) - 1)
    while i < j:
        (holder[i], holder[j]) = (holder[j], holder[i])
        i += 1
        j -= 1
    return ' '.join(holder)
