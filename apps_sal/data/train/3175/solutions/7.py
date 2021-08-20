def triple_double(num1, num2):
    DECIMAL_BASE = 10
    tripples = []
    (previous, previous_previous) = (None, None)
    while num1:
        (num1, rem) = divmod(num1, DECIMAL_BASE)
        if rem == previous and previous == previous_previous:
            tripples.append(rem)
        previous_previous = previous
        previous = rem
    while num2:
        (num2, rem) = divmod(num2, DECIMAL_BASE)
        if rem == previous and rem in tripples:
            return 1
        previous = rem
    return 0
