def solomons_quest(arr):
    layer = x = y = 0
    for l, dir_, distance in arr:
        layer = [layer+l,0][layer+l<0]
        inc, dec, r = [1,0,-1,0][dir_], [0,1,0,-1][dir_], distance*2**layer
        x += inc * r ; y += dec * r
    return [y,x]
