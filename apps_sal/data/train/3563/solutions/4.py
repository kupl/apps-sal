import math
def distance(n):
    if n == 1:
        return 0
    if n <= 9:
        return 2 if n%2 else 1
    lower = math.ceil(n**0.5)-2 if math.ceil(n**0.5)%2 else math.ceil(n**0.5)-1
    cycle = list(range(lower, (lower+1)//2-1, -1)) + list(range((lower+1)//2+1, lower+2))
    return cycle[(n-lower**2-1) % len(cycle)]
