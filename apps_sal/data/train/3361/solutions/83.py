def sum_of_minimums(numbers):
    Z = []
    for i in numbers:
        Z.append(min(i))

    return(sum(Z))
