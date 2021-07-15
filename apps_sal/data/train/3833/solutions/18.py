def longest(s1, s2):
    result = ''
    for i in sorted(set(list(set(s1)) + list(set(s2)))):
        result += i
    return result
