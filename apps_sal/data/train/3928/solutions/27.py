import functools 
def billboard(name, price = 30):
    print(name,price)
    return functools.reduce(lambda x,y : x + y , list(map(lambda x : price, list(range(len(name))))))
