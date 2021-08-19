def gimme(input_array):
    d = {}
    for i, v in enumerate(input_array):
        d[i] = v
    x = sorted(list(d.items()), key=lambda x: x[1])
    return(x[1][0])
    # Implement this function
