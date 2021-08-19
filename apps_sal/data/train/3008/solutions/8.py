def sort_array(value):
    l = []
    st = ''
    for i in value:
        l.append(i)
    l.sort()
    for n in l:
        st += n
    return st
