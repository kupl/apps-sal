def quicksum(packet):
    result = 0
    
    for idx, char in enumerate(packet, 1):
        if char.isupper():
            result += idx * (ord(char) - 64)
        elif char == " ":
            continue
        else:
            return 0
    
    return result
