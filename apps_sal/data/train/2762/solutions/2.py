NUMBERS = "nil one two three four five six seven eight nine".split()

def scoreboard(s):
    return [ NUMBERS.index(w) for w in s.split() if w in NUMBERS ]
