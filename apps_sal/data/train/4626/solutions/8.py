def decode(string_):
    if not isinstance(string_, str):
        return 'Input is not a string'
    input = list(string_)
    output = []
    dic1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    dic2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(len(input)):
        alph = ''
        for j in range(len(input[i])):
            if input[i][j].isupper():
                alph += dic2[25 - dic2.index(input[i][j])]
            elif input[i][j].islower():
                alph += dic1[25 - dic1.index(input[i][j])]
            else:
                alph += ''.join(input[i][j])
        output.append(alph)
    return ''.join(output)
