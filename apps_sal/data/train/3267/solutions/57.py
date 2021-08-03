def well(x):
    if "good" in x:
        return "I smell a series!" if x.count("good") > 2 else "Publish!"
    return "Fail!"
