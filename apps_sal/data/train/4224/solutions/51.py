def dont_give_me_five(start,end):
    numbers = list(range(start,end + 1))
    n = 0
    for i in numbers:
        s = str(i)
        if "5" not in s:
            n += 1
    return n   # amount of numbers
