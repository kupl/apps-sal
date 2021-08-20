def values(limit):

    def is_palindrome(n):
        n = str(n)
        if len(n) in [0, 1]:
            return True
        return n[0] == n[-1] and is_palindrome(n[1:-1])
    print('Limit: {}'.format(limit))
    current = 2
    totals = [1]
    list_pal = []
    while True:
        number = current ** 2 + totals[-1]
        totals = [i for i in totals if number - i < limit]
        if len(totals) == 1 and totals != [1]:
            break
        for i in totals[:-1]:
            if is_palindrome(number - i) and (not number - i in list_pal) and (limit > number - i):
                list_pal.append(number - i)
        if is_palindrome(number) and (not number in list_pal) and (limit > number):
            list_pal.append(number)
        totals.append(number)
        current += 1
    print('Number of Palindrome in list: {}'.format(len(list_pal)))
    print('List of Palindrome: {}'.format(list_pal))
    return len(list_pal)
