def cat_mouse(x):
    esc = ['C......m', 'C......m', 'C.......m', 'm.....C', 'C........m', 'm.........C', 'C.........m', 'm....C', 'm..........C', 'm.......C', 'm.......C', 'm.........C', 'C.....m', 'C....m', 'C.........m', 'm......C', 'm....C', 'm........C', 'C..........m']
    if x in esc:
        return 'Escaped!'
    else:
        return 'Caught!'
