def reverseWords(str):
    arr = []
    str = str.split(' ')
    str = str[::-1]
    return ' '.join(str)
