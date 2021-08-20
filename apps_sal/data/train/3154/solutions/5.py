def color_2_grey(colors):
    res = []
    for row in colors:
        g_row = []
        for pix in row:
            g_pix = []
            for c in pix:
                g_pix.append(int(round(sum(pix) / 3, 0)))
            g_row.append(g_pix)
        res.append(g_row)
    return res
