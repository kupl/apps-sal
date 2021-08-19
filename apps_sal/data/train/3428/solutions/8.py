def scanner(qrcode):
    # Setup
    bitstring = ''
    row = 20
    row_iter = -1
    col = 20
    col_iter = 0

    # Collect bitstring
    while not(row == 13 and col == 0):
        if not ((row <= 8 and col <= 8) or (row <= 8 and col >= 13) or (row >= 13 and col <= 8) or row == 6 or col == 6):
            if (row + col - col_iter) % 2 == 0:
                bitstring += str(1 - qrcode[row][col - col_iter])
            else:
                bitstring += str(qrcode[row][col - col_iter])
        else:
            pass

        # Assign new row col coordinates
        row = row + (row_iter * col_iter)
        col_iter = 1 - col_iter
        # Change direction if necessary
        if (row == -1 or row == 21) and col_iter == 0:
            row_iter = row_iter * -1
            row += row_iter
            col -= 2

    # Determine string length and clean bitstring
    str_length = int(bitstring[4:12], 2)
    bitstring = bitstring[12:]  # Remove encoding mode / message length

    # Convert bits into ASCII and return
    chars = []
    for b in range(0, str_length):
        byte = bitstring[b * 8:(b + 1) * 8]
        chars.append(chr(int(byte, 2)))
    return ''.join(chars)
