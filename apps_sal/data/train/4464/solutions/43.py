def feast(beast, dish):
    return ''.join(beast.split())[0]==''.join(dish.split())[0] and ''.join(beast.split())[-1]==''.join(dish.split())[-1]
