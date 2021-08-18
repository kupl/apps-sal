def to_leet_speak(str):
    output = ''

    leet_dict = {
        "A": '@',
        "B": '8',
        "C": '(',
        "D": 'D',
        "E": '3',
        "F": 'F',
        "G": '6',
        "H": '
        "I": '!',
        "J": 'J',
        "K": 'K',
        "L": '1',
        "M": 'M',
        "N": 'N',
        "O": '0',
        "P": 'P',
        "Q": 'Q',
        "R": 'R',
        "S": '$',
        "T": '7',
        "U": 'U',
        "V": 'V',
        "W": 'W',
        "X": 'X',
        "Y": 'Y',
        "Z": '2',
        " ": ' '
    }
    for letter in str:
        letter = letter.replace(letter, leet_dict[letter])
        output += letter
    return output
