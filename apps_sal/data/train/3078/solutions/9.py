from statistics import mean
def array_center(a):
    m, avg = min(a), mean(a)
    return [i for i in a if -m<(i-avg)<m]
