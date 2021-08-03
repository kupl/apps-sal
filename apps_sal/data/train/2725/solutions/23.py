def gimme(input_array):
    get = input_array.__getitem__
    return 3 - min(list(range(3)), key=get) - max(list(range(3)), key=get)
