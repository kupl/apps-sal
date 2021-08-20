def scanner(qrcode):
    finding_patterns = {((0, 9), (0, 9)), ((len(qrcode) - 8, len(qrcode)), (0, 9)), ((0, 9), (len(qrcode) - 8, len(qrcode)))}
    timing_patterns = {((9, len(qrcode) - 8), (6, 7)), ((6, 7), (9, len(qrcode) - 8))}
    function_patterns = {(x, y) for ((x0, x1), (y0, y1)) in finding_patterns | timing_patterns for x in range(x0, x1) for y in range(y0, y1)}
    reading = ((x, 2 * y - (y < 4) - i) for y in range(len(qrcode) // 2, 0, -1) for x in (reversed, iter)[y % 2](list(range(len(qrcode)))) for i in range(2))
    bits = ''.join((str((x + y ^ ~qrcode[x][y]) & 1) for (x, y) in reading if (x, y) not in function_patterns))
    return bytes((int(bits[i:i + 8], 2) for i in range(12, 12 + int(bits[4:12], 2) * 8, 8))).decode()
