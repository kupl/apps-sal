def duty_free(price,
              discount,
              holiday_cost):


    discount_amount = discount / 100. * price
    if (discount_amount):

        return holiday_cost // discount_amount

    return holiday_cost

