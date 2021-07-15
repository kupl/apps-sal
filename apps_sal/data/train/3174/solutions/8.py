def derivative(eq):
    r = '+'.join([s for s in [derive(w) for w in eq.replace('+', ' ').replace('-', ' -').replace('-x', '-1x').split()] if s])
    return r.replace('+-','-') if r else '0'

def derive(term):
    if 'x' not in term: return ''
    if '^' not in term:    
        return term.split('x')[0] if term.split('x')[0] else '1'
    a, b = [int(w) if w else 1 for w in term.split('x^')]
    a, b = a * b, b - 1
    return ('' if a == 1 else str(a)) + 'x' + ('^' + str(b) if b > 1 else '')
