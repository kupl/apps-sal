def narcissistic(n):
    s = str(n)
    l = len(s)
    return n == sum((int(d) ** l for d in s))


def is_narcissistic(*numbers):
    return all((str(n).isdigit() and narcissistic(int(n)) for n in numbers))
