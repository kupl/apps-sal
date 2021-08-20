def get_age(age):
    for (index, character) in enumerate(age):
        if character.isnumeric():
            return int(character)
