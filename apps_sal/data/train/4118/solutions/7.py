weapons = ['Laval-Shado Valious', 'Cragger-Vengdualize', 'Lagravis-Blazeprowlor', 'Crominus-Grandorius', 'Tormak-Tygafyre', 'LiElla-Roarburn']


def identify_weapon(character):
    return next((weapon for weapon in weapons if weapon.startswith(character)), 'Not a character')
