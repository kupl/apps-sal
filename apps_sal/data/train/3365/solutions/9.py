def format_poem(s):
    a, r = s.split('.'), []
    for k,i in enumerate(a):
        if k == 0:r.append(i.lstrip())
        else:r.append('\n'+i.lstrip())
    return ('.'.join(r)).rstrip('\n')

