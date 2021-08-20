def is_narcissistic(*args):

    def check(n):
        n = str(n)
        l = len(n)
        return int(n) == sum((int(d) ** l for d in n))
    return all((str(arg).isdigit() and check(int(arg)) for arg in args))
