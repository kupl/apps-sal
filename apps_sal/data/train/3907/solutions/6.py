import operator

funcs = {'0F12': operator.add, 'B7A2': operator.sub, 'C3D9': operator.mul}


def communication_module(packet):
    instruction, one, two = packet[4:8], int(packet[8:12]), int(packet[12:16])

    result = funcs[instruction](one, two)

    if result > 9999:
        result = 9999
    elif result < 0:
        result = 0

    return '{}FFFF{:0>4}0000{}'.format(packet[:4], result, packet[16:])
