def tongues(code):
    AsT = ""
    for i in code:
        if i == "i":
            AsT = AsT + "o"
        elif i == "t":
            AsT = AsT + "n"
        elif i == "a":
            AsT = AsT + "e"
        elif i == "d":
            AsT = AsT + "r"
        elif i == "f":
            AsT = AsT + "g"
        elif i == "y":
            AsT = AsT + "u"
        elif i == "c":
            AsT = AsT + "l"
        elif i == "s":
            AsT = AsT + "h"
        elif i == "w":
            AsT = AsT + "m"
        elif i == "v":
            AsT = AsT + "k"
        elif i == "q":
            AsT = AsT + "z"
        elif i == "p":
            AsT = AsT + "b"
        elif i == "j":
            AsT = AsT + "x"
        elif i == "o":
            AsT = AsT + "i"
        elif i == "n":
            AsT = AsT + "t"
        elif i == "e":
            AsT = AsT + "a"
        elif i == "r":
            AsT = AsT + "d"
        elif i == "g":
            AsT = AsT + "f"
        elif i == "u":
            AsT = AsT + "y"
        elif i == "l":
            AsT = AsT + "c"
        elif i == "h":
            AsT = AsT + "s"
        elif i == "m":
            AsT = AsT + "w"
        elif i == "k":
            AsT = AsT + "v"
        elif i == "z":
            AsT = AsT + "q"
        elif i == "b":
            AsT = AsT + "p"
        elif i == "x":
            AsT = AsT + "j"
        elif i == "I":
            AsT = AsT + "O"
        elif i == "T":
            AsT = AsT + "N"
        elif i == "A":
            AsT = AsT + "E"
        elif i == "D":
            AsT = AsT + "R"
        elif i == "F":
            AsT = AsT + "G"
        elif i == "Y":
            AsT = AsT + "U"
        elif i == "C":
            AsT = AsT + "L"
        elif i == "S":
            AsT = AsT + "H"
        elif i == "W":
            AsT = AsT + "M"
        elif i == "V":
            AsT = AsT + "K"
        elif i == "Q":
            AsT = AsT + "Z"
        elif i == "P":
            AsT = AsT + "B"
        elif i == "J":
            AsT = AsT + "X"
        elif i == "O":
            AsT = AsT + "I"
        elif i == "N":
            AsT = AsT + "T"
        elif i == "E":
            AsT = AsT + "A"
        elif i == "R":
            AsT = AsT + "D"
        elif i == "G":
            AsT = AsT + "F"
        elif i == "U":
            AsT = AsT + "Y"
        elif i == "L":
            AsT = AsT + "C"
        elif i == "H":
            AsT = AsT + "S"
        elif i == "M":
            AsT = AsT + "W"
        elif i == "K":
            AsT = AsT + "V"
        elif i == "Z":
            AsT = AsT + "Q"
        elif i == "B":
            AsT = AsT + "P"
        elif i == "X":
            AsT = AsT + "J"
        else:
            AsT = AsT + i
    return AsT
