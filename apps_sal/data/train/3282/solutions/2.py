def how_many_times(annual_price, individual_price):
    count = 0
    totalCost = 0
    while totalCost < annual_price:
        totalCost += individual_price
        count += 1
    return count
