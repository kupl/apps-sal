def disarium_number(num):
    it = list(str(num))
    count = 1
    true = 0

    for i in it:
        true += int(i) ** count
        count += 1
    if true == num:
        return "Disarium !!"
    else:
        return "Not !!"
