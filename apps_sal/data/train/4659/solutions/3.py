def numberAndIPaddress(s):
    if '.' in s:
        binary = ''.join(('{:08b}'.format(int(i)) for i in s.split('.')))
        return str(int(binary, 2))
    else:
        binary = '{:032b}'.format(int(s))
        res = [str(int(binary[i:i + 8], 2)) for i in range(0, len(binary), 8)]
        return '.'.join(res)
