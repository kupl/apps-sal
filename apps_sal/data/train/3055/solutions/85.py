def sum_str(a, b):
    numbers = []
    for i in (a, b):
        if i == "":
            i = 0
            numbers.append(i)
        else:
            numbers.append(int(i))
    return str(sum(numbers))
