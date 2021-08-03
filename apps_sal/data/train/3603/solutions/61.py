def lovefunc(flower1, flower2):
    return all([any([flower1 % 2 == 0, flower2 % 2 == 0]), any([flower1 % 2 == 1, flower2 % 2 == 1])])
