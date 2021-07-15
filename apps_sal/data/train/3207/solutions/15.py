def reverseWords(s):
    arr = s.split()
    arr = arr[::-1]
    str = ''
    for el in arr:
        str +=el+' '
    return str[:-1]
