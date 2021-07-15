def well(x):
    count = x.count("good")
    if count <= 2 and count >= 1:
        return "Publish!"
    elif count > 2:
        return "I smell a series!"
    else:
        return "Fail!"
        

