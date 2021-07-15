def spinning_rings(im, om):
    a,b,res,d = im,1,1,abs(om - im)
    while a != b:
        x = 1
        if a - b > 2: x = (a-b)//2
        if a < b: x = min(a + 1, om - b + 1)
        if b == im + 1 or om < im and a == im: x = d
        if a - b == 1: x = min(d,min(a,om-b))
        a,b = (a - x) % (im+1), (b + x) % (om+1)
        res += x
    return res
