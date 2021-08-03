def how_many_years(*dates):
    years = [int(date.split('/')[0]) for date in dates]
    return abs(years[0] - years[1])
