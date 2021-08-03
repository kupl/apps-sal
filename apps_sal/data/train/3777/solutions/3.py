def quicksum(packet):
    if not packet.replace(" ", "").isalpha() or not packet.isupper():
        return 0
    return sum((i + 1) * (1 + ord(l) - ord("A")) if l.isalpha() else 0 for i, l in enumerate(packet))
