def duty_free(price, discount, holiday_cost):
    actual_price = price * discount / 100

    count = 0
    total = 0
    while total < holiday_cost:
        total += actual_price
        count += 1

    return count - 1
