def super_size(n):
    li = list(str(n))  
    li.sort()     
    li.reverse()  
    temp = ''
    for i in range(len(li)):
        temp += li[i]
    return int(temp)
