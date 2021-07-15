def black_and_white(h,w,c):
    li = [[]]
    i = j = current = 0
    while i < len(c):
        current += c[i]
        if current > w:
            temp = current - w
            if c[i] - temp != 0 : li[j].append([['b', 'w'][i & 1], c[i] - temp])
            c[i] = temp ; j += 1
            li.append([]) ; current = 0
            continue
        li[j].append([['b', 'w'][i & 1], c[i]]) ; i += 1
        
    for i in range(len(li)):
        if li[i][0][0] != 'b' : li[i].insert(0, ['b', 0])
        if li[i][-1][0] != 'w' : li[i].append(['w', 0])    
    return [[j[1] for j in i] for i in li]
