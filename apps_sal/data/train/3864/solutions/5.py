def int32_to_ip(int32):
    """
    The solution involves bitwise AND of int32 and a mask that we can shift around.
    Say we have the number 17194 (0b0100001100101010). This can be divided into 2
    bytes: 01000011 and 00101010.
    We can AND this with a byte that is filled with 1s - 255 (0b11111111), shifted
    left by a certain amount of bytes to get the digits in that byte:
    01000011 00101010 # 17194
    11111111 00000000 # 255 << 8
    01000011 00000000 # 17194 & 255 << 8
    However, we need to shift this value *back* to get a number within (0,255)
    inclusive, as required, so shift right by the same amount.
    """
    first = (int32 & (255 << 24)) >> 24
    second = (int32 & (255 << 16)) >> 16
    third = (int32 & (255 << 8)) >> 8
    fourth = int32 & 255
    return f"{first}.{second}.{third}.{fourth}"
