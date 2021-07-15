def layers (n):
    level, i = 1, 1
    continuer = True
    while continuer :
        x = i * i
        if x < n :
            level += 1
            i += 2
        elif n <= x:
            return level

