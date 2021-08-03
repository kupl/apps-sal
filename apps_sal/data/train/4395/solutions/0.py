def next_higher(value):
    s = f'0{value:b}'
    i = s.rfind('01')
    s = s[:i] + '10' + ''.join(sorted(s[i + 2:]))
    return int(s, 2)
