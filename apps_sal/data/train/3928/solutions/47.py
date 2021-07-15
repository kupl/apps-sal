def billboard(name, price=30):
    letters = 1
    new_price = 0
    while letters <= len(name):
        new_price = new_price + price
        letters = letters + 1
    return new_price
        
        

