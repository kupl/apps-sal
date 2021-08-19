def lovefunc(flower1, flower2):
    if flower1 % 2 and (not flower2 % 2) or (not flower1 % 2 and flower2 % 2):
        return True
    else:
        return False
