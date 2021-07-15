def persistence(n):
    if str(n) == 1:
        return 0
    count = 0
    while len(str(n)) > 1:
        total = 1
        for i in str(n):
            total *= int(i)
        n = total
        count += 1
    return count
