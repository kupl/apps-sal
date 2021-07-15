from itertools import cycle
def lamps(a):
    dif=lambda a,b:sum(x!=y for x,y in zip(a,b))
    return min(dif(a,cycle([1,0])),dif(a,cycle([0,1])))
