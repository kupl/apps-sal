def create_array(n):
    res = []
    i = 1
    while n > len(res):
        res.append(i)
        i += 1
    return res
print(create_array(5))
