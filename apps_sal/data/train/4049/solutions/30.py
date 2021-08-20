def monkey_count(n):
    amount = []
    count = 1
    for i in range(n):
        amount.append(count)
        count = count + 1
    return amount
