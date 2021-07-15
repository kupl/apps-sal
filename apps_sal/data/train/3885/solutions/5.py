def values(high):
    s = set()
    num = 1
    while num * num < high:
        temp = num + 1
        total = num * num + temp * temp
        while total < high:
            if str(total) == str(total)[::-1]:
                s.add(total)
            temp += 1
            total += temp * temp
        num += 1
    return len(s)
