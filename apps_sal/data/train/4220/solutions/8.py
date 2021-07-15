def equable_triangle(a,b,c):
    s = sum([a,b,c]) / 2
    return sum([a,b,c]) == (s*(s-a)*(s-b)*(s-c)) ** 0.5
