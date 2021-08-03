def well(x):
    return ("I smell a series!" if x.count("good") > 2
            else "Fail!" if x.count("good") < 1
            else "Publish!")
