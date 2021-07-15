def find_difference(a, b):
    count1 = 1
    count2 = 1
    for i in a:
        if i < 0:
            return abs(i)
        else:     
            count1 *=i
    for j in b:
        if j < 0:
            return abs(j)
        else:
             count2 *=j
    output = count1 - count2
    if output < 0:
        return abs(output)
    return output

