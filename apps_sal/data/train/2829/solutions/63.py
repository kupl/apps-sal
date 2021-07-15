def array_madness(a:[],b:[]):
    result = 0
    result2 = 0
    for i in a:
        result += i*i
    for i in b:
        result2 += i*i*i
    if result > result2:
        return True
    return False



