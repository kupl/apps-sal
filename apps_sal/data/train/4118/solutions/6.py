def identify_weapon(character):
    dict = {"Laval": "Shado Valious",
            "Cragger": "Vengdualize",
            "Lagravis": "Blazeprowlor",
            "Cragger": "Vengdualize",
            "Lagravis": "Blazeprowlor",
            "Crominus": "Grandorius",
            "Tormak": "Tygafyre",
            "LiElla": "Roarburn"}
    if character not in dict.keys():
        return "Not a character"
    return character + "-" + dict[character]
