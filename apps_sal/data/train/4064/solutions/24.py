def count_by(a, n):
    list =[]
    for x in range(1, n+1):
        list.append(x)
    list2=[]
    for x in list:
        list2.append(x*a)
    return list2

