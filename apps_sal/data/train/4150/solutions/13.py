def rot13(message):
    index = {}
    az = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    AZ = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    azT = az[13:] + az[0:13]
    AZT = AZ[13:] + AZ[0:13]
    t = {a: b for (a, b) in zip(az + AZ, azT + AZT)}
    return ''.join([t.get(i, i) for i in message])
