def reverseWords(str):
    arr = str.split(' ')
    arr.reverse()
    return ' '.join(arr).rstrip()
