def make_readable(n):
    return f'{n // 3600:02d}:{n % 3600 // 60:02d}:{n % 60:02d}'
