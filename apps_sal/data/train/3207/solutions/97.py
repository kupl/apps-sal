def reverseWords(str):
    arr = str.split(' ')
    arr = arr[::-1]
    return ' '.join(arr)
