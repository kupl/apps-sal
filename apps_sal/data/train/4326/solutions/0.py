def london_city_hacker(journey): 
    # your code here
    tube = 2.40
    bus = 1.50
    total_cost = 0.00
    count = 0
    for link in journey:
        if isinstance(link, str):
            total_cost += tube
            count = 0
        else:
            if count == 0:
                total_cost += bus
                count +=1
            else:
                count = 0
    return '£{:.2f}'.format(total_cost)

