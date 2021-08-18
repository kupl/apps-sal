def to_leet_speak(s):
    r = {".": ".", "!": "!", "?": "?", ",": ",", " ": " ", "A": '@', "B": '8', "C": '(', "D": 'D', "E": '3', "F": 'F', "G": '6', "H": '
    return ''.join(r[c] for c in s)
