import math
def solution(n):
    d=0
    if n - 0.25< math.floor(n):
        d=math.floor(n)
    elif n - 0.75< math.floor(n):
        d=math.floor(n)+0.5
    else:
        d=math.ceil(n)
    return d
