import re
import math


def switch_endian(n, bits):
    number_in_hex = hex(n)
    length = len(number_in_hex) - 2
    result = int(bits / 4)
    x = math.log(bits, 2).is_integer()
    if x == False:
        return None
    if length > result:
        return None
    if length <= result:
        diff = result - length
        number_in_hex = number_in_hex.replace('0x', '0' * diff)
        res_list = re.findall('[\da-z]{2}[^\da-z]*', number_in_hex)
        res_list = res_list[::-1]
        number_in_hex = ''.join(res_list)
        return(int('0x' + number_in_hex, 0))
