def sort_string(s, ordering):
    result = ''
    for i in ordering:
        if i in s and i not in result:
            result += i * s.count(i)
    return result + ''.join([c for c in s if c not in ordering])
