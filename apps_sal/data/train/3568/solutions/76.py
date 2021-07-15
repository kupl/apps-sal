def bumps(road):
    # your code here
    return "Car Dead" if len(list(filter(str.isalpha,road))) > 15 else 'Woohoo!'    

