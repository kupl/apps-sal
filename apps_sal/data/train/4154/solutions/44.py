def is_triangle(a, b, c):
    triangleList = [a,b,c]
    triangleList.sort()
    if triangleList[0]+triangleList[1] > triangleList[2]:
        return True
    else:
        return False

