def divisible_by(numbers, divisor):
    emptylist = []
    for eachnumber in numbers:
        if eachnumber % divisor == 0:
            emptylist.append(eachnumber)
    return emptylist
