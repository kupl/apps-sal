def bumps(road):
    count = 0
    for el in road:
        if el == "n":
            count+=1
    if count <= 15:
        return "Woohoo!"
    else:
        return "Car Dead"

