def digitize(n):
    num_array = []
    for number in str(n):
        num_array.insert(0, int(number))
    return num_array
