def solution(to_cur, values):
    rate = 1.1363636
    style = '{:,.2f}'
    if to_cur == 'EUR':
        rate = 1 / rate
        style += '€'
    else:
        style = '$' + style
    return [style.format(v * rate) for v in values]
