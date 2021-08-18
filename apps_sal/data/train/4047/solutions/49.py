def to_leet_speak(str):
    table = str.maketrans({'A': '@', 'B': '8', 'C': '(', 'E': '3', 'G': '6', 'H': '
    return str.translate(table)
