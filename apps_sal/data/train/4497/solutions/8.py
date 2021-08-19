def positive_to_negative(binary):
    n = len(binary)
    end = 0
    for i in range(n - 1, -1, -1):
        if binary[i] == 1:
            end = i
            break
    for i in range(end):
        binary[i] ^= 1
    return binary
