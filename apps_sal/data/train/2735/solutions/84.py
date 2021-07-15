def jumping_number(number):
    digits = list(map(int, f'{number}'))
    prev = digits.pop(0)
    while digits:
        curr = digits.pop(0)
        if curr != prev - 1 and curr != prev + 1:
            return 'Not!!'
        prev = curr
    return 'Jumping!!'
