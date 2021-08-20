def bar_triang(pointA, pointB, pointC):

    def mod(indx):
        return round(sum(list([_[indx] for _ in [pointA, pointB, pointC]])) / 3, 4)
    return [mod(0), mod(1)]
