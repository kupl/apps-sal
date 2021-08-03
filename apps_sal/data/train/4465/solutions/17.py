def super_size(n):
    li = list()
    p = ''
    for i in str(n):
        li.append((i))
    for j in range(len(li)):
        p += max(li)
        li.remove(max(li))
    return int(p)
