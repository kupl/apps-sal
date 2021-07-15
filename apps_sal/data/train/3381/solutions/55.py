def get_real_floor(n):
    floor=0
    if n>=1:
        floor-=1
    if n>=13:
        floor-=1
    return n + floor
