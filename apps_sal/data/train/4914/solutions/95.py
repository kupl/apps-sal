def position(alphabet):
    dictionary = {chr(96 + i): i for i in range(1, 27)}

    return "Position of alphabet: " + str(dictionary[alphabet])
