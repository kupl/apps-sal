def solution(to_cur, values):
    return [f'${v * 1.1363636:0,.2f}' if to_cur == 'USD' else f'{v / 1.1363636:0,.2f}€' for v in values]
