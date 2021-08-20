def identify_weapon(character):
    wep = {'Laval': 'Laval-Shado Valious', 'Cragger': 'Cragger-Vengdualize', 'Lagravis': 'Lagravis-Blazeprowlor', 'Crominus': 'Crominus-Grandorius', 'Tormak': 'Tormak-Tygafyre', 'LiElla': 'LiElla-Roarburn'}
    return wep.get(character, 'Not a character')
