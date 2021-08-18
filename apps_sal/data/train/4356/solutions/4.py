def colorful(number):
    lst = [int(d) for d in str(number)]

    if number > 9:
        if 0 in lst or 1 in lst:
            return False

        all, previous = lst, -1
        for digit in str(number):
            if previous != -1:
                lst.append(int(digit) * previous)
            previous = int(digit)

        if number > 99:
            total = 1
            for d in all:
                total *= d
            lst.append(total)

    return len(lst) == len(set(lst))
