def communication_module(packet):
    calc = 0
    if packet[4:8] == "0F12":
        calc = int(packet[8:12]) + int(packet[12:16])
    elif packet[4:8] == "B7A2":
        calc = int(packet[8:12]) - int(packet[12:16])
    elif packet[4:8] == "C3D9":
        calc = int(packet[8:12]) * int(packet[12:16])

    if calc < 0:
        calc = "0000"
    elif calc > 9999:
        calc = "9999"

    return packet[0:4] + "FFFF" + str(calc).zfill(4) + "0000" + packet[16:20]
