def symmetric_point(p, q):
    xp, yp, xq, yq = p+q
    xd, yd = abs(xp-xq), abs(yp-yq)
    return [xq+(xd if xp<xq else -xd), yq+(yd if yp<yq else -yd)]
