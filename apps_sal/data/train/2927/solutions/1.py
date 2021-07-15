def zombie_shootout(z, r, a):
    s = min(r*2, a)
    return f"You shot all {z} zombies." if s>=z else f"You shot {s} zombies before being eaten: { 'overwhelmed' if s==2*r else 'ran out of ammo' }."
