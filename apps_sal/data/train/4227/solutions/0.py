def complexSum(arr, sub={'1i': 'i', '-1i': '-i', '0i': '0'}):
    s = str(sum(complex(x.replace('i', 'j')) for x in arr)).replace('j', 'i')
    s = s.strip('()')
    s = s.replace('+0i', '')
    return sub.get(s, s)    
