def balanced_num(number):
    l = len(str(number))
    if l % 2 == 0:
        return "Balanced" if sum([int(x) for x in str(number)[:int(l / 2) - 1]]) == sum([int(x) for x in str(number)[int(l / 2) + 1:]]) else "Not Balanced"
    return "Balanced" if sum([int(x) for x in str(number)[:int(l / 2)]]) == sum([int(x) for x in str(number)[int(l / 2) + 1:]]) else "Not Balanced"
