def identify_weapon(character):
    tbl = {'Laval': 'Laval-Shado Valious', 'Cragger': 'Cragger-Vengdualize', 'Lagravis': 'Lagravis-Blazeprowlor', 'Crominus': 'Crominus-Grandorius', 'Tormak': 'Tormak-Tygafyre', 'LiElla': 'LiElla-Roarburn'}
    return tbl.get(character, 'Not a character')
