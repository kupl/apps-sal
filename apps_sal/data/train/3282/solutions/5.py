def how_many_times(annual_price, individual_price):
    result = 1
    while (result*individual_price) < annual_price:
        result += 1
    return result
