def calculate_age(y, c):
    if y<c:
        return "You are {} {} old.".format(c-y,("year" if c-y==1 else "years"))
    elif y>c:
        return "You will be born in {} {}.".format(y-c,("year" if y-c==1 else "years"))
    else:
        return "You were born this very year!"
