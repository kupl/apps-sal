def well(x):
    return ["Fail!", "Publish!", "Publish!", "I smell a series!"][x.count("good") if x.count("good") < 3 else 3]
