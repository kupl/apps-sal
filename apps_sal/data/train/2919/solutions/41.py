def encode(message, key):
    letters = {chr(97+x):x+1 for x in range(28)}
    return [letters[l]+int(add) for l,add in zip(message, list(str(key)) * len(message) )]
