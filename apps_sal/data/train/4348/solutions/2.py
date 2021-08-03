def calc_fuel(n):
    # Start coding! You can do it!
    time = n * 11
    dict = {"lava": time // 800, "blaze rod": (time % 800) // 120, "coal": ((time % 800) % 120) // 80, "wood": (((time % 800) % 120) % 80) // 15, "stick": (((time % 800) % 120) % 80) % 15}

    return dict
