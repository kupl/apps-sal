def dont_give_me_five(start, end):
    count = 0
    numbers = [str(x) for x in range(start, end + 1)]
    for number in numbers:
        if '5' not in number:
            count += 1
    return count
