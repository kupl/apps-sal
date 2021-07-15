def pseudo_sort(s): 
    s = ''.join(i for i in s if i.isalpha() or i is ' ')
    a =  sorted(i for i in s.split() if i[0].islower())
    b =  sorted((i for i in s.split() if i[0].isupper()),key=lambda x: x.lower(),reverse=True)
    return ' '.join(a+b)
