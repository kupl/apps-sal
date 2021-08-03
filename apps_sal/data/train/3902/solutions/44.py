def duty_free(price, discount, holiday_cost):
    discount /= 100
    price_with_discount = price * discount
    finish_price = 0
    count = 0
    while finish_price < holiday_cost:
        finish_price += price_with_discount
        if finish_price > holiday_cost:
            break
        count += 1
    return count
