def find_2nd_largest(arr):
    a, b = float('-inf'), float('-inf')

    for n in arr:
        if isinstance(n, int):
            if n > b:
                b = n
            if b > a:
                a, b = b, a

    return None if a == b else b
