def billboard(name, price=30):
    # your code here - note that in Python we cannot prevent the use of the
    # multiplication, but try not to be lame and solve the kata in another way!

    total = 0
    # for i in name:
    #   total += price
    # return total

    return sum(total + price for _ in name)
