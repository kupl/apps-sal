def add(a, b):
    longer = max(len(a), len(b))
    a, b = [x.zfill(longer) for x in [a, b]]
    p = {'000': '00', '001': '10',
         '010': '10', '011': '01',
         '100': '10', '101': '01',
         '110': '01', '111': '11'}
    result = []
    c = '0'
    for x, y in zip(reversed(a), reversed(b)):
        r, c = p[x + y + c]
        result.append(r)
    if c == '1': result.append(c)
    return ''.join(reversed(result)).lstrip('0') or '0'
