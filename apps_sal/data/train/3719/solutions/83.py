def starting_mark(height):
    slope = (10.67-9.45)/(1.83-1.52)
    if height < 1.52:
        return round(9.45-(1.52-height)*slope, 2)
    elif height < 1.83:
        return round(10.67-(1.83-height)*slope, 2)
    else:
        return round(10.67+(height-1.83)*slope, 2)
