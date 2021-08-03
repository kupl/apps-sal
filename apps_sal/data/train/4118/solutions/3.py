def identify_weapon(character):
    weps = {'Laval': 'Shado Valious',
            'Cragger': 'Vengdualize',
            'Lagravis': 'Blazeprowlor',
            'Crominus': 'Grandorius',
            'Tormak': 'Tygafyre',
            'LiElla': 'Roarburn'}
    try:
        return "{}-{}".format(character, weps[character])
    except:
        return "Not a character"
