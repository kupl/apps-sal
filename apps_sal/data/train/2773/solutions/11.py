def calculate_years(principal, interest, tax, desired):
    y=0
    while principal<desired:
        extra=principal*interest
        principal+=extra-tax*extra
        y+=1
    return y
