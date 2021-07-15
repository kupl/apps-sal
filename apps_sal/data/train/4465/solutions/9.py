def super_size(n):
    digits = sorted([d for d in str(n)],reverse=True)
    return int( ''.join(digits))


