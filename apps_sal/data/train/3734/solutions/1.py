from random import randint

def roll(desc, verbose=False):
    try:
        a, x, *d = desc.replace(' ', '').replace('-', '+-').replace('+', 'd').split('d')
        dice = [randint(1, int(x)) for _ in range(int(a or '1'))]
        modifier = sum(map(int, d))
        if verbose:
            return {'dice': dice, 'modifier': modifier}
        else:
            return sum(dice) + modifier
    except:
        return False
