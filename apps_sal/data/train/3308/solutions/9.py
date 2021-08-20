def parity_bit(binary):
    lst_bin = binary.split()
    final = []
    for i in range(len(lst_bin)):
        n = lst_bin[i][:-1].count('1')
        if lst_bin[i][-1:] == '0':
            if n % 2 != 0:
                final.append('error')
            else:
                final.append(lst_bin[i][:-1])
        if lst_bin[i][-1:] == '1':
            if n % 2 != 0:
                final.append(lst_bin[i][:-1])
            else:
                final.append('error')
    return ' '.join(final)
