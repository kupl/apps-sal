def process_data(data):
    r = 1
    for d in data:
        r *= d[0] - d[1]
    return r
