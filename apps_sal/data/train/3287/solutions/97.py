def mouth_size(animal):
    result = ""
    animal_recase = animal.lower()
    if animal_recase == "alligator":
        result = "small"
    else:
        result = "wide"
    return result
