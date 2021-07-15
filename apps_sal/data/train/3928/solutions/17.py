def billboard(name, price = 30):
    cost = 0
    print(name)
    for i in range(len(name)):
        cost += price
    return cost
    #your code here - note that in Python we cannot prevent the use of the
    #multiplication, but try not to be lame and solve the kata in another way!

