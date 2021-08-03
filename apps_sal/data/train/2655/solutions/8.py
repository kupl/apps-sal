def duck_shoot(ammo, aim, ducks):
    output = ''
    kills = int(ammo * aim)
    for duck in ducks:
        if duck == '2':
            if kills > 0:
                output += 'X'
                kills -= 1
            else:
                output += duck
        else:
            output += duck
    return output
