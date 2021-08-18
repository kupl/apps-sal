def dont_give_me_five(start, end):
    numbers = []

    for i in range(start, end + 1):
        if '5' in str(i):
            continue
        else:
            numbers.append(i)

    return len(numbers)
