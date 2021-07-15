def pascal(p):
    if p == 1: return [[1]]
    output = [[1],[1,1]]
    last = [1,1]
    count = 2
    while count < p:
        new = []
        new.append(1)
        for i in range(count-1):
            new.append(last[i]+last[i+1])
        new.append(1)
        output.append(new)
        last = new
        count += 1
    return output
