def string_to_number(s):
    # Ok, let's get real.  Converting from a string of numbers to an integer is easy.
    # here's the one line that solves this:
    #     return int(s)
    #
    # So let's have some fun...
    # Let's convert the number to binary first!
    binary = bin(int(s))
    print(s + ' in binary: ' + binary)
    # Then hexadecimal
    hexa = hex(int(binary, 2))  # yeah, cheating by turning binary to decimal, then to hex
    print(binary + ' in hex: ' + hexa)
    # Wonder what happens if we reverse the characters in the hex string?
    remove0x = hexa.replace('0x', '')
    reversed = '0x' + remove0x[::-1]
    print('Reversed: ' + reversed)
    # Well that was pointless!
    # Hmm... take the ascii code of each character in hexa (other than '0x', multiply it by
    # 10 to the power of (length of the string - index of the character) ?
    multiplied = ''
    for i in range(len(remove0x)):
        multiplied += chr(ord(remove0x[i]) * (10 * (len(remove0x) - i)))
    print('Multiplied: ' + multiplied)
    #
    # We're getting nowhere fast.
    see = 0
    for i in multiplied:
        see += ord(i)
    print('Ascii added: ' + str(see))
    # Nope.
    rereversed = '0x' + reversed.replace('0x', '')[::-1]
    print(rereversed + ' is ' + reversed + ' reversed again.')
    if '-' in rereversed:
        rereversed = '-' + rereversed.replace('-', '')
    # If the number is negative, let's get the negative sign in the right place
    print('If we change that to integer and return it...  Hmm!')
    #
    # Could it be that simple???
    return int(rereversed, 16)
