def is_triangle(a, b, c):
    if (a + b) > c and (a + c) > b and (b + c) > a:
     print("You can make a triangle with these numbers")
     return True
    else:
     print("You cannot make a triangle with these numbers")
     return False
