def evaporator(content, evap_per_day, threshold):
    n = 0
    daily_content = content
    threshold_vol = threshold / 100 * content
    while daily_content > threshold_vol:
        daily_content = daily_content - (evap_per_day / 100 * daily_content)
        n += 1
    print(f"The {n}th day the evaporator is useless")
    return n
