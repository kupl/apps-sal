def lottery(s):

    result = ''

    for i in s:
        if i.isdigit() and i not in result:
            result += i

    return result or 'One more run!'
