def billboard(name, price=30):
    total = 0
    i = 0
    while i < len(name):
        total += price
        i += 1
    return total
    # your code here - note that in Python we cannot prevent the use of the
    # multiplication, but try not to be lame and solve the kata in another way!
