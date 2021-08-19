# If a sequence has very few elements, it is best to compute enough of it at first
# And then just iterate over it
res = [528, 825, 1561, 1651, 4064, 4604, 5346, 6435, 5795, 5975]


def equal_sigma1(nMax):
    return sum(x for x in res if x <= nMax)
