def kebabize(s):
    l = [i for i in s if i.isalpha() ]
    if s.isdigit():
        return ''
    if s.isupper():
        return '-'.join(l).lower()
    for i in range(len(l)-1):
        if (l[i].islower() or l[i].isupper()) and l[i+1].isupper():
            l[i] += '-'
    return ''.join(l).lower()
