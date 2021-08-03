def lovefunc(flower1, flower2):
    return bool(flower1 % 2 and not flower2 % 2 or flower2 % 2 and not flower1 % 2)
