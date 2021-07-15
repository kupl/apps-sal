from string import ascii_lowercase as buttons, digits as buttons2

remote = {}
#assign cordinates, assuming cords of a, (x,y) = (0,0)
for temp_x, button in enumerate(buttons):
    remote[button] = (temp_x % 5, temp_x // 5)
for temp_x, button in enumerate(buttons2[1::]):
    remote[button] = (temp_x % 3 + 5, temp_x // 3)
remote["."], remote["@"], remote["0"] = (5, 3), (6, 3), (7, 3)
remote["z"], remote["_"], remote["/"] = (5, 4), (6, 4), (7, 4)


def tv_remote(word):
    presses = ix = iy = 0
    for letter in word:
        x, y = remote[letter]
        presses += abs(x-ix) + abs(y-iy) +1
        ix, iy = x, y
    return presses
