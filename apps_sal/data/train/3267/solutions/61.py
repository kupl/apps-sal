def well(x):
    counter = 0 
    for i in x:
        if i == "good":
            counter += 1
    if counter < 1:
        return "Fail!" 
    elif counter <= 2:
        return "Publish!"
    elif counter >2:
        return "I smell a series!"
