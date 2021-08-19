def scan_column(qrcode, x0, y0, height, bottom_to_top=True):
    result = []
    if bottom_to_top:
        height_range = list(range(0, height * -1, -1))
    else:
        height_range = list(range(height))
    for dy in height_range:
        y = y0 + dy
        x = x0
        result.append(qrcode[y][x] ^ (x + y + 1) % 2)
        x = x0 - 1
        result.append(qrcode[y][x] ^ (x + y + 1) % 2)
    return result


def byte_to_int(byte):
    return int(''.join(map(str, byte)), 2)


def raw_data_to_str(raw_data):
    return ''.join([chr(byte_to_int(byte)) for byte in raw_data])


def scanner(qrcode):
    result = []
    result += scan_column(qrcode, 20, 20, 12, bottom_to_top=True)
    result += scan_column(qrcode, 18, 9, 12, bottom_to_top=False)
    result += scan_column(qrcode, 16, 20, 12, bottom_to_top=True)
    result += scan_column(qrcode, 14, 9, 12, bottom_to_top=False)
    encoding_raw = result[:4]
    length_raw = result[4:12]
    length = byte_to_int(length_raw)
    data_raw = [result[12 + 8 * i:12 + 8 * (i + 1)] for i in range(length)]
    data = raw_data_to_str(data_raw)
    return data
