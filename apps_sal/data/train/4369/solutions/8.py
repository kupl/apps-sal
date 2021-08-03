import struct


def is_negative_zero(n):
    return struct.pack('>d', n) == b'\x80\x00\x00\x00\x00\x00\x00\x00'
