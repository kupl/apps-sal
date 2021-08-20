def args_count(*a1, **a2):
    total = sum((1 for i in a1))
    total += sum((1 for i in a2))
    return total
