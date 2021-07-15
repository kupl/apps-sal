def max_tri_sum(numbers):
    x=[]
    for i in numbers:
        if i not in x:
            x.append(i)
    x=sorted(x)
    return sum(x[-3:])
