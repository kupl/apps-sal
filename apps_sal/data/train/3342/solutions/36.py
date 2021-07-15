def pattern(n):
    empty_s = ''
    if isinstance(n, str):
        return '1'
    else:
        if n >= 1:
            for i in range(1, n + 1):
                empty_s += f'{str ( i ) * i}\n'
            return empty_s[:-1]
        else:
            return ""
