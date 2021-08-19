def pattern(n):
    nums = '1234567890'
    str_nums = nums * (n // 10) + nums[:n % 10]
    return '\n'.join((' ' * (n - i - 1) + str_nums + ' ' * i for i in range(n)))
