def valid_parentheses(s):
    p = '()'
    s = ''.join([e  for e in s if e in '()'])
    while p in s:#
        s = s.replace(p,'')
    return not s
