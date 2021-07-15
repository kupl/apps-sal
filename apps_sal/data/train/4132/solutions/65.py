def correct_tail(body, tail):
    animal = []
    for letter in body:
        animal.append(letter)
    if animal[-1] == tail:
        return True
    else:
        return False
