def reverseWords(str):
    arr = list(str.split())
    arr.reverse()
    return ' '.join([i for i in arr])

