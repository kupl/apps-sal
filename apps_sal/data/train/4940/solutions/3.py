def shut_the_gate(farm):
    r = ''
    for i, c in enumerate(farm):
        left, right = farm[:i][::-1], farm[i + 1:]
        if c in 'HCR':
            if '|' not in left or '|' not in right:
                c = '.'
        elif c in 'VA':
            for e in (left + farm[i + 1:][::-1]).split('|')[0] + (right + farm[:i]).split('|')[0]:
                if e + c in 'HVHARV':
                    c = '.'
        r += c
    return r
