def to_leet_speak(str):
    alfabe = {'A': '@', 'B': '8', 'C': '(', 'D': 'D', 'E': '3', 'F': 'F', 'G': '6', 'H': '
    for i in list(alfabe.keys()):
        if i in str:
            str = str.replace(i, alfabe[i])
    return str
