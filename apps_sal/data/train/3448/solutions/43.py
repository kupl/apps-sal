def f(n):
    if type(n) is int and n >= 1:
        number_of_elements = n / 2
        total_elements = (n + 1) * number_of_elements
        return total_elements
    else:
        return None
