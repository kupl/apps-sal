def number(lines):
    sum=[]
    for i in range(len(lines)):
        a = str(i+1)+": "+lines[i]
        sum.append(a)
    return sum
