def vowel_start(st):
    rst = ''
    for e in st:
        if not e.isalnum():
            continue
        e = e.lower()
        if e in 'aeiou':
            rst += f' {e}'
        else:
            rst += e
    return rst.lstrip()
