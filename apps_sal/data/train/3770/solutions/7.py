def to_1D(x, y, size):
    c = 0
    for i in range(size[1]):
        for j in range(size[0]):
            if x ==j and y ==i:
                return c
            c+=1
    
def to_2D(n, size):
    c = 0
    for i in range(size[1]):
        for j in range(size[0]):
            if n == c:
                return j, i
            c+=1
