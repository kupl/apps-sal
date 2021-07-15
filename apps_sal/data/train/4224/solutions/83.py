def dont_give_me_five(start,end):
    count = 0
    for number in range(start, (end + 1)):
        number_as_str = str(number)
        if "5" not in number_as_str:
            count += 1

    return count
