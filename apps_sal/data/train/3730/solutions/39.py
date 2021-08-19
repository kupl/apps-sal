def capitalize(s):
    array = list(s)
    (output1, output2) = ([], [])
    for (i, letter) in enumerate(array):
        if i % 2 == 0:
            output1.append(letter.upper())
            output2.append(letter.lower())
        else:
            output1.append(letter.lower())
            output2.append(letter.upper())
    output3 = ''.join(output1)
    output4 = ''.join(output2)
    return [output3, output4]
