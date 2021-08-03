
# determinant for this particular case
def det(m):
    return (m[0][0] * (m[1][1] - m[2][1]) +
           m[1][0] * (m[2][1] - m[0][1] ) +
            m[2][0] * (m[0][1] - m[1][1]) )


def count_col_triang(input_):
    # init variables
    colored = []
    colors = {}
    n_tri = []
    ncol = 0

    # separate points by colors
    for point, color in input_:
        if color not in colors:
            colors[color] = ncol
            colored.append([])
            n_tri.append(0)
            ncol += 1
        colored[colors[color]].append(point)

    # for each 3 points: calculate deteminant to determine if they form a triangle
    for color, cpts in enumerate(colored):

        if len(cpts) < 3:
            continue
        for k in range(len(cpts)):
            for l in range(k + 1):
                for m in range(l + 1):
                    if det([cpts[k], cpts[l], cpts[m]]) != 0:
                        n_tri[color] += 1

    # find maximum number of triangles
    tmax = max(n_tri)

    # find corresponding colors
    clrmax = []
    if tmax > 0:
        for color in sorted(colors):
            if n_tri[colors[color]] == tmax:
                clrmax.append(color)
        clrmax.append(tmax)

    return [len(input_), ncol, sum(n_tri), clrmax]
