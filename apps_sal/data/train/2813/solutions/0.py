def switcher(arr):
    d = {str(i): chr(123-i) for i in range(1,27)}
    d.update({'27':'!'})
    d.update({'28':'?'})
    d.update({'29':' '})
    d.update({'0':''})
    return ''.join([d[str(i)] for i in arr])
