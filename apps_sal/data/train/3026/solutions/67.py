def min_value(digits):
    # your code here
    lostlist = ""
    for i in sorted(list(set(digits))):
        lostlist += str(i)
    return int(lostlist)
