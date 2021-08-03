def solution(to_cur, value):
    return ['${:,.2f}'.format(x * 1.1363636) if to_cur == 'USD' else '{:,.2f}€'.format(x / 1.1363636) for x in value]
