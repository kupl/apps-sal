def identify_weapon(character):
    d = {'Laval': 'Shado Valious', 'Cragger': 'Vengdualize', 'Lagravis': 'Blazeprowlor', 'Crominus': 'Grandorius', 'Tormak': 'Tygafyre', 'LiElla': 'Roarburn'}
    return f'{character}-{d[character]}' if character in d else 'Not a character'
