def process_data(data):
    output = 1
    for sub_list in data:
        output *= sub_list[0] - sub_list[1]
    return output
