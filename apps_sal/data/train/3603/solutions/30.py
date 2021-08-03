def lovefunc(flower1, flower2):
    even_odd = []
    if flower1 % 2 == 0:
        even_odd.append("even")
    else:
        even_odd.append("odd")
    if flower2 % 2 == 0:
        even_odd.append("even")
    else:
        even_odd.append("odd")

    return even_odd.count("odd") == 1
