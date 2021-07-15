def feast(beast, dish):
    beast = beast.lower()
    dish = dish.lower()
    if beast[-1] == dish[-1] and beast[0] == dish[0]:
           return True
    else:
           return False
           
feast("Faris","Mangos")
