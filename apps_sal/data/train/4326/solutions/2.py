def london_city_hacker(journey):
    prices = []
    
    for stop in journey:
        prices.append(2.4 if type(stop) is str else 1.5)
        if prices[-2:] == [1.5, 1.5]:
            prices[-1] = 0
    
    return f"£{sum(prices):.2f}"
