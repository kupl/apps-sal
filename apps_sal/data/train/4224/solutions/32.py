def dont_give_me_five(start, end):
    count = 0

    for i in range(start, end + 1):
        valid = True
        for j in str(i):
            if j == "5":
                valid = False
        if valid:
            count += 1

    return count   # amount of numbers
