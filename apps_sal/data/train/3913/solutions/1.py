def solution(to_cur, values):
    (rate, fmt) = {'USD': (1.1363636, '${:,.2f}'), 'EUR': (1 / 1.1363636, '{:,.2f}€')}[to_cur]
    values = [v * rate for v in values]
    return list(map(fmt.format, values))
