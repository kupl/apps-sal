def arr(*n):
    print(*n)
    res = []
    if(n == () or n == 0):
        return []
    else:
        for i in range((*n)):
            res.append(i)
        return res
