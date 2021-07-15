def is_divide_by(number, *args):
    return all((not number % i) for i in args)
