def to_leet_speak(str):
    dic = {
        "A": '@',
        "B": '8',
        "C": '(',
        "E": '3',
        "F": 'F',
        "G": '6',
        "H": '#',
        "I": '!',
        "L": '1',
        "O": '0',
        "S": '$',
        "T": '7',
        "Z": '2'
    }
    return(''.join(dic.get(i, i) for i in str))
