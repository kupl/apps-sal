def identify_weapon(character):
    data = {
        'Laval': 'Shado Valious',
        'Cragger': "Vengdualize",
        "Lagravis": "Blazeprowlor",
        "Crominus": "Grandorius",
        "Tormak": "Tygafyre",
        "LiElla": "Roarburn"
    }
    try:
        return "%s-%s" % (character, data[character])
    except KeyError:
        return "Not a character"
