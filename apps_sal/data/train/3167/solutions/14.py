def twos_difference(lst):
    concat = []
    for number in lst:
        if int(number) + 2 in lst:
            concat.append((int(number), int(number) + 2))
    return sorted(concat)
