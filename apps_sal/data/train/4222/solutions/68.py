def get_size(w,h,d):
    #your code here
    area = ((d * h) * 2 ) + ((w * d) * 2) + ((w * h)* 2)
    volume = w * h * d
    return [area,volume]
