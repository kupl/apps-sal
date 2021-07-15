def duty_free(price, discount, holiday_cost):
        proc = discount / 100 
        price_new = proc * price
        final = holiday_cost / price_new
        return int(final)
