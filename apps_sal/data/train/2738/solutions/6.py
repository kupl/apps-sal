def i_tri(s):
    if s == 0:
        return "Starting Line... Good Luck!"
    swim = 2.4
    bicycle = 112
    marathon = 26.2
    distance = swim + bicycle + marathon
    if s > distance:
        return "You're done! Stop running!"

    txt = "Swim" if s <= swim else \
        "Bike" if s <= (swim + bicycle) else \
        "Run"

    remaining = distance - s
    obj = {f"{txt}": f"{remaining:.2f} to go!"}

    return obj
