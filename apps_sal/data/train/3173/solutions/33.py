def create_array(n):
    res=[1]
    i=2
    while max(res) != n: 
        res.append(i)
        i +=1
    return res
