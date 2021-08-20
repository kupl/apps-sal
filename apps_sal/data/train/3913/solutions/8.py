def solution(to_cur, value):
    return [f'${i * 1.1363636:,.2f}' if to_cur == 'USD' else f'{i / 1.1363636:,.2f}€' for i in value]
