def reverseWords(str):
    result = ''
    s1 = str.split(' ')
    print(s1)
    s2 = s1[::-1]
    print(s2)
    result = ' '.join(s2)
    return result
