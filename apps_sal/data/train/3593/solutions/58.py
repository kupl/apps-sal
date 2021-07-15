def capitalize(s,ind):
    count=0
    output = []
    for i in s:
        if ind.count(count) > 0:
            output.append(i.upper())
            count+=1
        else:
            output.append(i)
            count+=1
    return(''.join(output))
        

