def string_to_number(s):
    binary = bin(int(s))
    print(s + ' in binary: ' + binary)
    hexa = hex(int(binary, 2))
    print(binary + ' in hex: ' + hexa)
    remove0x = hexa.replace('0x', '')
    reversed = '0x' + remove0x[::-1]
    print('Reversed: ' + reversed)
    multiplied = ''
    for i in range(len(remove0x)):
        multiplied += chr(ord(remove0x[i]) * (10 * (len(remove0x) - i)))
    print('Multiplied: ' + multiplied)
    see = 0
    for i in multiplied:
        see += ord(i)
    print('Ascii added: ' + str(see))
    rereversed = '0x' + reversed.replace('0x', '')[::-1]
    print(rereversed + ' is ' + reversed + ' reversed again.')
    if '-' in rereversed:
        rereversed = '-' + rereversed.replace('-', '')
    print('If we change that to integer and return it...  Hmm!')
    return int(rereversed, 16)
