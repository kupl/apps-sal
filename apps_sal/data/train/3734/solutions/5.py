from random import randint


def roll(desc, verbose=False):
    if not desc:
        return False
    desc = desc.replace(' ', '')
    for letter in desc:
        if letter.isalpha() and letter != 'd':
            return False
    if desc != desc.replace('++', '+').replace('--', '-'):
        return False

    operations = '-+'
    rolls = []
    result = ''

    for each in operations:
        desc = desc.replace(each, f' {each} ')
    for i, part in enumerate(desc.split(' ')):
        if 'd' in part:
            part = resolve(part, verbose)
            rolls.extend(part)
            result += str(sum(part))
        else:
            result += part
    result = eval(result)
    if verbose:
        return {'dice': rolls, "modifier": result - sum(rolls)}
    return result


def resolve(dice, verbose=None):
    dice = dice.split('d')
    d, t = list(map(int, dice)) if dice[0] != '' else (1, int(dice[1]))
    return [randint(1, t) for _ in range(d)]
