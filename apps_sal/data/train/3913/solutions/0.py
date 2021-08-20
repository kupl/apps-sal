def solution(to, lst):
    (dolSym, eurSym, power) = ('', '€', -1) if to == 'EUR' else ('$', '', 1)
    return [f'{dolSym}{v * 1.1363636 ** power:,.2f}{eurSym}' for v in lst]
