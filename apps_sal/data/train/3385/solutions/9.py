def longest(s):
    result = []
    ordx = 0
    for i in s:
        if ord(i) >= ordx:
            ordx = ord(i)
            result.append(i)
        else:
            result.append('|')
            result.append(i)
            ordx = ord(i)
    return max(''.join(result).split('|'), key=len)
