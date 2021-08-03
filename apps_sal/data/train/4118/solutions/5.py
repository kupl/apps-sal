def identify_weapon(character):
    weapons = {'Laval': 'Shado Valious', 'Cragger': 'Vengdualize', 'Lagravis': 'Blazeprowlor', 'Crominus': 'Grandorius', 'Tormak': 'Tygafyre', 'LiElla': 'Roarburn'}
    return '%s-%s' % (character, weapons[character]) if character in weapons else 'Not a character'
