def is_divisible(n,*args):
    return all(n % i == 0 for i in args)
