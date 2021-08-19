def reverseWords(s):
    arr = s.split(' ')
    arr = arr[::-1]
    return ' '.join(arr)
