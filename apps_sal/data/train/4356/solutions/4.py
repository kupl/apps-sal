def colorful(number):
    lst = [int(d) for d in str(number)]

    if number > 9:
        # no need to compute : if 1 ==> previous * 1 == previous, if 0 ==> previous * 0 == 0
        if 0 in lst or 1 in lst:
            return False

        all, previous = lst, -1
        for digit in str(number):
            # not the first time
            if previous != -1:
                lst.append(int(digit) * previous)
            previous = int(digit)

        # if 1 or 2 digits : multiplication of all numbers is already added to the list
        if number > 99:
            total = 1
            for d in all:
                total *= d
            lst.append(total)

    return len(lst) == len(set(lst))
