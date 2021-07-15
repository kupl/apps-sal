def digitize(n):
    x = ','.join(str(n))[::-1]
    result=[]
    for i in x.split(','):
        result.append(int(i))
    return result
