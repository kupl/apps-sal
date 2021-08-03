def find_digit(num, nth):
    snum = str(num)
    if nth <= 0:
        return -1
    try:
        if snum[(-nth)].isnumeric:
            return int(snum[(-nth)])
    except:
        return 0
