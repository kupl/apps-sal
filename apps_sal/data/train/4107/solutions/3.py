from datetime import datetime


def half_life(*p):
    D = sorted((datetime.strptime(x, '%Y-%m-%d') for x in p))
    return (D[1] + (D[1] - D[0])).strftime('%Y-%m-%d')
