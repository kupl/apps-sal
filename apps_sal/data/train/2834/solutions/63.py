def symmetric_point(p, q):
    px, py = p
    qx, qy = q
    xdist = px - qx
    ydist = py - qy
    return [qx - xdist, qy - ydist]
