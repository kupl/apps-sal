def billboard(name, price=30):
    # your code here - note that in Python we cannot prevent the use of the
    # multiplication, but try not to be lame and solve the kata in another way!
    # for each character in name, add price once
    return sum(price for x in name)
