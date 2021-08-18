def solution(to_cur, value):
    rate = 1.1363636
    return list([f'${x*rate:,.2f}' for x in value]) if to_cur == 'USD' else list([f'{x/rate:,.2f}€' for x in value])
