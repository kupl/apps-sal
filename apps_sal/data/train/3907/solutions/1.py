import re
from operator import add, sub, mul

instructions = {
    '0F12': add,
    'B7A2': sub,
    'C3D9': mul,
}


def communication_module(packet):
    header, instruction, data1, data2, footer = re.findall('....', packet)
    result = instructions[instruction](int(data1), int(data2))
    return '{}FFFF{:04}0000{}'.format(header, min(max(result, 0), 9999), footer)
