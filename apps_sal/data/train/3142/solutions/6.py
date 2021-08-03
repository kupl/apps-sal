def seven_ate9(str_):
    previous, current = str_, str_.replace("797", "77")
    while previous != current:
        previous, current = current, current.replace("797", "77")
    return current
