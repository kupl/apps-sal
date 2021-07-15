from statistics import mean

def avg_array(arrs):
    return list(map(mean,zip(*arrs)))
