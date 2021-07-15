def spread(func, args):
    if args != ():
        return func(*args)
    else:
        return func()
