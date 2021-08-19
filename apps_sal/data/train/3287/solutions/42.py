def mouth_size(animal):
    # casefold makes case insensitive string matching
    if animal.casefold() == "alligator":
        return "small"
    else:
        return "wide"
