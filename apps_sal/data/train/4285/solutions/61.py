def find_slope(points):
    top_of_equation = points[3]-points[1]
    bot_of_equation = points[2]-points[0]

    if bot_of_equation == 0:
        return "undefined"
    return str(int(round(top_of_equation / bot_of_equation)))

