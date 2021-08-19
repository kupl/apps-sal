def replace_dots(st):
    print(('==>> ', st))
    if len(st) == 0:
        return ''
    num_dots = 0
    for lletra in st:
        if lletra == '.':
            num_dots += 1
    if num_dots > 0:
        return st.replace('.', '-')
    else:
        return 'no dots'
