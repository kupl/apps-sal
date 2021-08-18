def to_leet_speak(s):
    leet = {'A': '@', 'B': '8', 'C': '(', 'D': 'D', 'E': '3', 'F': 'F', 'G': '6', 'H': '
    return s.upper().translate(s.maketrans(leet))
