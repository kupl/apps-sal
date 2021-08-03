def billboard(name, price=30):
    print(('name:', name))
    return sum([price for x in name])
    # your code here - note that in Python we cannot prevent the use of the
    # multiplication, but try not to be lame and solve the kata in another way!
