def find_unknown_number(x,y,z):
    for i in range(1,1000):
        if i%3 == x and i%5 == y and i%7 == z:
                return i
