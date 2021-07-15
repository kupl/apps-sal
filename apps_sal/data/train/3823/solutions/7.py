def deep_count(a):
    b = []
    while  a:
        for i in a:
            if type(i) == list:
                a.extend(i)
                a.remove(i)
                a.append('1')
            else:
                b.append(i)
                a.remove(i)
    return len(b)
