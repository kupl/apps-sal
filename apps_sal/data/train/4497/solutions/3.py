def positive_to_negative(binary):
    binary = [not i for i in binary]
    for i in range(len(binary) - 1, -1, -1):
        if binary[i]:
            binary[i] = 0
        else:
            binary[i] = 1
            break

    return binary
