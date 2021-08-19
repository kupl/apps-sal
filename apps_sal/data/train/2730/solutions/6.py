def tickets(people):
    bill25 = 0
    bill50 = 0
    bill100 = 0
    for bill in people:
        if bill == 25:
            bill25 += 1
        elif bill == 50:
            bill50 += 1
            if bill25 == 0:
                return 'NO'
            bill25 -= 1
        elif bill == 100:
            bill100 += 1
            if bill50 > 0 and bill25 > 0:
                bill50 -= 1
                bill25 -= 1
            elif bill25 >= 3:
                bill25 = bill25 - 3
            else:
                return 'NO'
    return 'YES'
