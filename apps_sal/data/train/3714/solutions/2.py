from re import findall

def encoder(data):
    base = ""
    dictionary = {base: 0}
    output = []
    
    for char in data:
        curr = base + char
        if curr in dictionary:
            base = curr
        else:
            output.append(f"{dictionary[base]}{char}")
            dictionary[curr] = len(dictionary)
            base = ""
    
    if base:
        output.append(f"{dictionary[base]}")
    
    return "".join(output)


def decoder(data):
    dictionary = [""]
    
    for idx, char in findall("(\d+)([A-Z]?)", data):
        dictionary.append(dictionary[int(idx)] + char)
    
    return "".join(dictionary)
