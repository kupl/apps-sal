def nth_even(n):
    result = range(n * 2)
    for elem in result[::-1]:
        if elem % 2 == 0:
            return elem
