def positive_to_negative(binary):
    if sum(binary) == 0:
        return binary
    steps = []
    index = 0
    zero_counter = 0
    for bin_num in binary:
        if binary[index] == 0:
            zero_counter += 1
            binary[index] = 1
        elif binary[index] == 1:
            binary[index] = 0
        steps.append(0)
        index += 1
    fill = list(steps)
    fill[-1] = 1
    index = len(binary) - 1
    while index >= 0:
        if index != len(binary) - 1:
            binary[index] += fill[index] + steps[index + 1]
        else:
            binary[index] += fill[index]
        if binary[index] == 2:
            binary[index] -= 2
            steps[index] += 1
        index -= 1
    return binary
