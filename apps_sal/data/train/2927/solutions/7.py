def zombie_shootout(z, r, a):
    n = min(z, r * 2, a)
    return f'You shot all {n} zombies.' if n == z else f"You shot {n} zombies before being eaten: {('ran out of ammo' if n == a and n != r * 2 else 'overwhelmed')}."
