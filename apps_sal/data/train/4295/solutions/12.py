def balanced_num(number):
    a = str(number)
    b = a[:len(a) // 2]
    c = a[len(a) // 2 + 1:]
    d = a[:len(a) // 2 - 1]
    if len(a) % 2 == 1:
        if sum([int(i) for i in b]) == sum([int(x) for x in c]):
            return "Balanced"
        return "Not Balanced"
    if len(a) % 2 == 0:
        if sum([int(i) for i in d]) == sum([int(x) for x in c]):
            return "Balanced"
        return "Not Balanced"
