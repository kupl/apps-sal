weapon_map = {
    'Laval': 'Laval-Shado Valious',
    'Cragger': 'Cragger-Vengdualize',
    'Lagravis': 'Lagravis-Blazeprowlor',
    'Crominus': 'Crominus-Grandorius',
    'Tormak': 'Tormak-Tygafyre',
    'LiElla': 'LiElla-Roarburn',
}


def identify_weapon(character):
    return weapon_map.get(character, 'Not a character')
