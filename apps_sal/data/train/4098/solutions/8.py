def new_numeral_system(number):
    output = []
    for i in range(0, (ord(number) - ord('A')) // 2 + 1):
        output.append(chr(i + 65) + ' + ' + chr(ord(number) - i))
    return output
