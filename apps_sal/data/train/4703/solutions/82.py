from statistics import mean
def bar_triang(pointA, pointB, pointC):
    return [round(mean(x), 4) for  x in zip(pointA, pointB, pointC)]
