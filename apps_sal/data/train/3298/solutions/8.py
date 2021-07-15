def avg_array(arrs):
    x=[]
    for i in zip(*arrs):
        x.append(sum(i)/len(arrs))
    return x

