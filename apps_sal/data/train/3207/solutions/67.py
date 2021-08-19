def reverseWords(s: ''):
    s = s.split()
    result = ''
    for i in s:
        result = i + ' ' + result
    return result.strip(' ')
