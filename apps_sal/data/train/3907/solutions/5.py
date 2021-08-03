from operator import add, sub, mul


def communication_module(packet):
    part = [packet[i:i + 4] for i in range(0, len(packet), 4)]
    res = {'0F12': add, 'B7A2': sub, 'C3D9': mul}[part[1]](int(part[2]), int(part[3]))
    res = max(0, min(res, 9999))
    return part[0] + f'FFFF{str(res).zfill(4)}0000' + part[4]
