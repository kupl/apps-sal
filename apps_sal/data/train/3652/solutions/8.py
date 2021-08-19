def button_sequences(seqR, seqB):
    result = ''
    prec_r = '0'
    prec_b = '0'
    seqR = list(seqR)
    seqB = list(seqB)
    for (r, b) in zip(seqR, seqB):
        if r == b and r == '1' and (prec_r != '1') and (prec_b != '1'):
            result += 'R'
        elif r != b and r == '1' and (prec_r != '1'):
            result += 'R'
        elif r != b and b == '1' and (prec_b != '1'):
            result += 'B'
        elif prec_r == prec_b and prec_r == '1' and (r == '1') and (b != r) and (result[len(result) - 1] != 'R'):
            result += 'R'
        elif prec_r == prec_b and prec_r == '1' and (b == '1') and (b != r) and (result[len(result) - 1] != 'B'):
            result += 'B'
        prec_r = r
        prec_b = b
    return result
