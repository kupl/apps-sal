def max_product(a):
    b=list(a)
    max_number=max(b)
    b.remove(max_number)
    second_number=max(b)
    return max_number * second_number
