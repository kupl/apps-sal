def well(x):
    results = ""
    good_count = x.count("good")
    if good_count == 0:
        results = "Fail!"
    elif good_count <= 2:
        results = "Publish!"
    else :
        results = "I smell a series!"
    return results
