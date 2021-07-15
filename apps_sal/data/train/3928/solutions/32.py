def billboard(name, price=30):
    sum = 0
    for letter in name:
        sum = sum + price
        
    return sum
