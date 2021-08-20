def angle(n):
    if n > 2:
        return int((180 - 360 / n) * n + 0.5)
    else:
        print('error')
        return ''
