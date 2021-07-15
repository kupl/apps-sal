def vaporcode(s):
    result = ''
    for x in s:
        if x == ' ':
            continue
        result = result + x.upper() + '  '
    return result[:len(result)-2]

