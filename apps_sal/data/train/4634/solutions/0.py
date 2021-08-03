def pac_man(size, pacman, enemies):
    px, py = pacman
    mx, my, Mx, My = -1, -1, size, size
    for x, y in enemies:
        if x < px and x > mx:
            mx = x
        if y < py and y > my:
            my = y
        if x > px and x < Mx:
            Mx = x
        if y > py and y < My:
            My = y
    return (Mx - mx - 1) * (My - my - 1) - 1
