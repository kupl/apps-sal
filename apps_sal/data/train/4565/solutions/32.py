def replace_dots(s):
    if s == '':
        return ''
    for i in s:
        if not '.' in s:
            return 'no dots'
        else:
            for j in range(len(s)):
                if s[j] == '.':
                    v = s.replace(s[j], '-')
                    return v
