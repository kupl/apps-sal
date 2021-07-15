def well(x):
    return "I smell a series!" if x.count("good") > 2 else "Publish!" if x.count("good") >= 1 else "Fail!"
