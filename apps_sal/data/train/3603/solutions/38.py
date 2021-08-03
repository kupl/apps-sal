def lovefunc(flower1, flower2):
    petal1 = flower1 % 2
    petal2 = flower2 % 2
    if petal1 == 0 and petal2 > 0:
        return True
    if petal1 > 0 and petal2 == 0:
        return True
    if petal1 == 0 and petal2 == 0:
        return False
    if petal1 > 0 and petal2 > 0:
        return False
