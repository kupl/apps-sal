dating_range = \
    lambda x: "%s-%s" % ((str(int(x - 0.10 * x))), (str(int(x + 0.10 * x)))) if x <= 14 \
    else "%s-%s" % ((str(int(x / 2 + 7))), (str(int(x - 7) * 2)))
