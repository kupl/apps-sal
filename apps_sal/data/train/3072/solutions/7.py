def narcissistic(n):
    try:
        k = len(str(n))
        return sum(d**k for d in map(int, str(n))) == int(n)
    except ValueError:
        return False

def is_narcissistic(*args):
    return all(map(narcissistic, args))
