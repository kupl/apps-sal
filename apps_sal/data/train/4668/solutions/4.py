def is_divisible_by_6(s):
    xs = [s.replace('*', str(i)) for i in range(10)]
    return [x.lstrip('0') or '0' for x in xs if int(x) % 6 == 0]
