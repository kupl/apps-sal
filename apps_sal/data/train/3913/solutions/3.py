def solution(to_cur, lst):
    (rate, fmt) = {'USD': (1.1363636, '${:,.2f}'), 'EUR': (0.88, '{:,.2f}€')}[to_cur]
    return [fmt.format(val * rate) for val in lst]
