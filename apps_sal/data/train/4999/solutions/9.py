
def capital(capitals):
    output = []

    i = 0
    for key1, key2 in capitals:
        if key1 == "country":
            output.append(
                f"The capital of {capitals[i]['country']} is {capitals[i]['capital']}")
        if key1 == "state":
            output.append(
                f"The capital of {capitals[i]['state']} is {capitals[i]['capital']}")
        i += 1
    return output
