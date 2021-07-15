def is_triangle(a, b, c):
    if not a + b > c or not a + c > b or not b + c >a:
        print(('AB pair',a+b,c))
        print(('AC pair',a+c,b))
        print(('BC pair',b+c,a))
        return False
    else:
        return True

