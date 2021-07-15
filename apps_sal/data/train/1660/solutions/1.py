import re
def simplify(poly):
    terms = {}
    for sign, coef, vars in re.findall(r'([\-+]?)(\d*)([a-z]*)', poly):
        sign = (-1 if sign == '-' else 1)
        coef = sign * int(coef or 1)
        vars = ''.join(sorted(vars))
        terms[vars] = terms.get(vars, 0) + coef
    # sort by no. of variables
    terms = sorted(list(terms.items()), key=lambda v_c: (len(v_c[0]), v_c[0]))
    return ''.join(map(format_term, terms)).strip('+')

def format_term(xxx_todo_changeme):
    (vars, coef) = xxx_todo_changeme
    if coef == 0:
        return ''
    if coef == 1:
        return '+' + vars
    if coef == -1:
        return '-' + vars
    return '%+i%s' % (coef, vars)

