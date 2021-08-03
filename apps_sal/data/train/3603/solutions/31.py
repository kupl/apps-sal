def lovefunc(flower1, flower2):
    def a(x, y): return True if (x % 2 == 0 and y % 2 == 1) or (x % 2 == 1 and y % 2 == 0) else False
    return a(flower1, flower2)
