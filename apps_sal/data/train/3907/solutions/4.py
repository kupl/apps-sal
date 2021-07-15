def communication_module(packet):
    part = [packet[i:i+4] for i in range(0, len(packet), 4)]
    d = {'0F12':'+','B7A2':'-','C3D9':'*'}
    res = eval(f'{int(part[2])}{d[part[1]]}{int(part[3])}')
    res = max(0, min(res, 9999))
    return part[0]+f'FFFF{str(res).zfill(4)}0000'+part[4]
