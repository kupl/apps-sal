def increment_string(strng):
    import re
    if re.search('\\d+$', strng):
        x = re.findall('(\\d+)$', strng)[0]
        y = str(int(x) + 1)
        return re.sub('(\\d+)$', '', strng) + '0' * (len(x) - len(y)) + y
    else:
        return strng + '1'
