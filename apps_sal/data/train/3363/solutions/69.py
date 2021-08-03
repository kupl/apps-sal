def evaporator(content, evap_per_day, threshold):
    '''
    receives:
    - content of gas in ml.
    - percentaje of content lost every day.
    - threshold as a percentage of the original capacity below which the cooler does not work.

    returns:
    - the nth day on which the evaporator will be out of use.
    '''
    days = 0
    threshold_in_ml = content * threshold / 100

    while content > threshold_in_ml:
        days += 1
        content = content - (content * evap_per_day / 100)

    return days
