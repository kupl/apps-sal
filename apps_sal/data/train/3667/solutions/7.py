def mid_endian(n):
    hex_str = hex(n)[2:].zfill(len(hex(n)[2:]) + len(hex(n)[2:]) % 2).upper()
    cut = [hex_str[i:i + 2] for i in range(0, len(hex_str) - 1, 2)]
    cut += [] if len(cut) % 2 else ['']
    return ''.join(cut[1::2][::-1] + cut[0:1] + cut[2::2])
