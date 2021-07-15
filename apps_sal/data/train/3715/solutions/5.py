lst = [5]
for i in range(2, 14):
    x = 5**i
    lst.append(x)
    temp = lst[:]
    for j in temp[:-1]:
        lst.append(j+x)

def nth_chandos_number(n):
    return lst[n-1]
