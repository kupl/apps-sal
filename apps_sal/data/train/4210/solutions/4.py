def process_data(data):
    result = 1
    for item in data:
        result *= item[0] - item[1]
    return result
