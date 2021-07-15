def mouth_size(animal):
    animal = str(animal).lower()
    if animal=="alligator":
        return "small"
    else:
        return "wide"
s = mouth_size("alligator")
print(s)
