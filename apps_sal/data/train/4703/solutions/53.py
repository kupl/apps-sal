from statistics import mean
def bar_triang(pointA, pointB, pointC): 
    return [round(mean(row),4) for row in zip(pointA,pointB,pointC)]

