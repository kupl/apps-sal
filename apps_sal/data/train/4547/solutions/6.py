def more_zeros(s):
    output = []
    for ch in s:
        bin_rep = f'{ord(ch):b}'
        if bin_rep.count('0') > bin_rep.count('1') and ch not in output:
            output.append(ch)
    return output
