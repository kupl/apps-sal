from math import cos, sin, radians


def coordinates(d, r):

    def convert(x):
        return round(r * x(radians(d)), 10)
    return (convert(cos), convert(sin))
