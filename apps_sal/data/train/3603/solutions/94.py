def lovefunc( flower1, flower2 ):
    if flower1%2 == 0:
        return not flower2%2 == 0
    else:
        return flower2%2 == 0
