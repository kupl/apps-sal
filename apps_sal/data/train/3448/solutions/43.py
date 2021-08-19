def f(n):
    # 1 + 2 + 3 + n-2 + n-1 + n
    # 1+n + 2+n-1 + 3+n-2 + ...
    if type(n) is int and n >= 1:
        number_of_elements = n / 2
        total_elements = (n + 1) * number_of_elements
        return total_elements
    else:
        return None
