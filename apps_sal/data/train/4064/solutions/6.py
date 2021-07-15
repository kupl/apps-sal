def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    num = x
    results = [x]

    for i in range(n-1):
        num += x
        results.append(num)

    return results
        

