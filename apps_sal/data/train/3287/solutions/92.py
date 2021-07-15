def mouth_size(animal): 
    mouth = ""
    if animal.casefold() != "alligator":
        mouth = "wide"
    else:
        mouth = "small"
    return mouth
