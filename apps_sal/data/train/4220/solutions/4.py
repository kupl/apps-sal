def equable_triangle(a,b,c):
    perimeter=a+b+c
    sp=perimeter/2
    area=(sp*(sp-a)*(sp-b)*(sp-c))**0.5
    if perimeter==area: return True
    else: return False
