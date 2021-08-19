def lovefunc(flower1, flower2):
    odd1 = flower1 % 2
    odd2 = flower2 % 2
    if (odd1 or odd2) and (not (odd1 and odd2)):
        return True
    else:
        return False
