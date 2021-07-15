def duty_free(price, discount, holiday_cost):
    savings = price - (discount/100)*price
    print(price,discount,holiday_cost,savings,holiday_cost//savings)
    return holiday_cost // (price-savings)
