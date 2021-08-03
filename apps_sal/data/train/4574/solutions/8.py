# -*- coding: utf-8 -*-
def build_a_wall(x=None, y=None):
    if not all([isinstance(x, int), isinstance(y, int)])\
            or x < 1 or y < 1:
        return None
    elif x * y > 10000:
        return "Naah, too much...here\'s my resignation."
    else:
        halfbrick = "■"
        brick = 2 * halfbrick
        mortar = "|"
        wall = ""
        for i in range(x):
            if i % 2 == 0:
                wall = brick + (mortar + brick) * (y - 1) + wall
            else:
                wall = halfbrick + (mortar + brick) * (y - 1) + mortar + halfbrick + wall
            wall = "\n" + wall if i < x - 1 else wall
        return wall
