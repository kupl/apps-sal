def spider_to_fly(spider, fly):
    from cmath import exp, pi, rect

    def coordinates(hexpoint):
        t, r = hexpoint
        return rect(int(r), 'ABCDEFGH'.index(t) * pi / 4)
    return abs(coordinates(spider) - coordinates(fly))
