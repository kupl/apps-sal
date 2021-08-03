def mouth_size(animal):
    return "small" if ''.join([x.lower() for x in animal]) == "alligator" else "wide"
