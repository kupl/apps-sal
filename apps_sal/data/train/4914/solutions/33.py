def position(letter):
    alpahabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(0, len(alpahabet)):
        if alpahabet[i] == letter:
            return 'Position of alphabet: ' + str(i + 1)
