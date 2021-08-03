def decipher_message(message):
    if not message:
        return ""
    res = []
    for i in range(0, len(message), int(len(message)**0.5)):
        res.append(message[i:i + int(len(message)**0.5)])
    solution = ""
    for i in range(len(res)):
        for j in range(len(res[i])):
            solution += res[j][i]
    return solution
