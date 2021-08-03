def correct(m, n, bits):

    msg = [bits[i * n: (i + 1) * n] for i in range(m)]
    msgt = [''.join([bits[i] for i in range(j, m * n, n)]) for j in range(n)]

    msg_row_parity = ''.join([str(x.count('1') % 2) for x in msg])
    msg_col_parity = ''.join([str(x.count('1') % 2) for x in msgt])

    bits_row_parity = bits[-m - n:-n]
    bits_col_parity = bits[-n:]

    if msg_row_parity == bits_row_parity and msg_col_parity == bits_col_parity:
        return bits
    if msg_row_parity == bits_row_parity:
        return bits[:-n] + msg_col_parity
    if msg_col_parity == bits_col_parity:
        return bits[:-m - n] + msg_row_parity + bits[-n:]

    err_row = [i for i in range(m) if bits_row_parity[i] != msg_row_parity[i]][0]
    err_col = [i for i in range(n) if bits_col_parity[i] != msg_col_parity[i]][0]

    err_bit_msg = msg[err_row][err_col]
    cor_bit = str(abs(int(err_bit_msg) - 1))
    msg_pos = err_row * n + err_col
    return bits[:msg_pos] + cor_bit + bits[msg_pos + 1:]
