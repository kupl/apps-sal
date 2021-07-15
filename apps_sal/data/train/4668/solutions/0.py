def is_divisible_by_6(s):
    all_numbers = [ int(s.replace('*', str(n))) for n in range(10) ]
    return [ str(n) for n in all_numbers if n % 6 == 0 ]
