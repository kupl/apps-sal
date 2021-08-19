VALID = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def quicksum(packet):
    return 0 if (set(packet) - set(VALID)) else sum(VALID.index(char) * i for i, char in enumerate(packet, 1))

#    checksum = 0
#    for char in packet:
#        if not char in VALID:
#            return 0
#        checksum += VALID.index(char)
#    return checksum

    # in respect to given instructions (packet has to begin and end with uppercase)
#    if any(not char.isupper() for char in (packet[0], packet[-1])):
#        return 0
