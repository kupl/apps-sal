def well(x):
    return "I smell a series!" if sum(1 if i == "good" else 0 for i in x) > 2 else "Publish!" if 3 > sum(1 if i == "good" else 0 for i in x) > 0 else "Fail!"
