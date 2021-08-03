def balanced_num(number):
    number = str(number)
    if len(number) % 2 != 0:
        middle = len(number) // 2
        leftside = number[:middle]
        rightside = number[middle + 1:]
        sumofleft = sum(list([int(x) for x in leftside]))
        sumofright = sum(list(int(x) for x in rightside))
        if sumofleft == sumofright:
            return 'Balanced'
        else:
            return 'Not Balanced'
    if len(number) % 2 == 0:
        middle = len(number) // 2
        leftside = number[:middle - 1]
        rightside = number[middle + 1:]
        sumofleft = sum(list([int(x) for x in leftside]))
        sumofright = sum(list(int(x) for x in rightside))
        if sumofleft == sumofright:
            return 'Balanced'
        else:
            return 'Not Balanced'
