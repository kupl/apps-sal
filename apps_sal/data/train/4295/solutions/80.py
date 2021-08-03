def balanced_num(number):
    x = str(number)
    z = [int(i) for i in x]

    if len(z) <= 2:
        return "Balanced"
    elif len(z) == 3:
        return "Balanced" if z[0] == z[-1] else "Not Balanced"
    else:
        if len(z) > 3 and len(z) % 2 == 0:
            middle_1 = int(len(z) / 2) - 1
            middle_2 = int(len(z) / 2)
            first, mid, second = z[:middle_1], z[middle_1:middle_2 + 1], z[middle_2 + 1:]
            return "Balanced" if sum(first) == sum(second) else "Not Balanced"
        elif len(z) > 3 and len(z) % 2 != 0:
            middle = int(len(z) // 2)
            first, mid, second = z[:middle], z[middle], z[middle + 1:]
            return "Balanced" if sum(first) == sum(second) else "Not Balanced"
