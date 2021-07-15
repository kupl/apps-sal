def two_decimal_places(n):
    decimal = int((n*100 - int(n*100))*10)
    print(decimal)
    if decimal <= -5:
        return (int(n*100)-1)/100
    elif decimal < 5:
        return int(n*100)/100
    else:
        return (int(n*100)+1)/100
