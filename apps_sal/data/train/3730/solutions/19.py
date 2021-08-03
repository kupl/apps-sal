def capitalize(s):
    s.lower()
    z = s.__len__()
    count = 1
    i = 0
    new_one = ''
    new_two = ''
    while i < z:
        if (i + 1) % 2 == 0 and i > 0:
            new_one = new_one.ljust(count, str(s[i].upper()))
            new_two = new_two.ljust(count, str(s[i]))
            count = count + 1
            i = i + 1
        else:
            new_two = new_two.ljust(count, str(s[i].upper()))
            new_one = new_one.ljust(count, str(s[i]))
            count = count + 1
            i = i + 1
    answer = [new_two, new_one]
    return answer
