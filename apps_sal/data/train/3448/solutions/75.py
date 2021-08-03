def f(n):
    if type(n) == int:
        counter = 0
        if n > 0:
            for i in range(n + 1):
                counter += i

        if counter > 0:
            return counter
        else:
            return None

    return None
