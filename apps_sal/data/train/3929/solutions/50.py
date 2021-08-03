def reverse(s):
    result = ''
    for i in s.split()[::-1]:
        result += i + ' '

    return result.rstrip()
