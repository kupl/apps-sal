def nerdify(txt):
    arr = []
    for i in txt:
        if i == 'a' or i == 'A':
            arr.append('4')
        elif i == 'e' or i == 'E':
            arr.append('3')
        elif i == 'l':
            arr.append('1')
        else:
            arr.append(i)
    return ''.join(arr)
