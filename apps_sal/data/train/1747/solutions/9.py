def sortme_sensei(name, ls, ref, p):
    ref = [val[0] for val in ref]
    ls = list(zip(ls, p))
    ls.sort(key=lambda x: ref.index(x[1]))
    return [val[0] for val in ls]


def crosstable(players, results):
    points, i = {v: [float(sum([val for val in x if val != None])), 0, x] for v, x in zip(players, results)}, 0
    for n in players:
        indo = results[i]
        for idx, num in enumerate(indo):
            if num == 1:
                points[n][1] += points[players[idx]][0]
            elif num == 0.5:
                points[n][1] += points[players[idx]][0] / 2
        i += 1
    D = [(p, pts[0], f"{pts[1]:.2f}") for p, pts in list(points.items())]
    sep_points, playa, ptsz, Sb = len(str(len(players))), len(max(players, key=len)) + 2, len(
        max([str(val[1]) for val in D], key=len)), \
        len(max([str(val[2]) for val in D], key=len))
    D.sort(key=lambda x: (-x[1], -float(x[2]), x[0].split()[1]))
    points = {k: [v[0], v[1], sortme_sensei(k, v[2], D, players)] for k, v in list(points.items())}
    string = "
        str(i).rjust(sep_points + 1) if i - 1 else str(i).rjust(sep_points) for i in range(1, len(players) + 1)) +
        "  " + "Pts".center(ptsz) + "  " + (
        "SB".center(Sb - 1)[:-1] if "SB".center(Sb - 1)[-1] == " " else "SB".center(Sb - 1)) + "\n"
    tempo, C="", 0
    for i in range(len(D)):
        tempo += str(i + 1 if D[i - 1][2] != D[i][2] or D[i - 1][1] != D[i][1] else "").rjust(sep_points) + "  "
            + D[i][0].ljust(playa)
        for idx, res in enumerate(points[D[i][0]][2]):
            if idx:
                tempo += res in [1, 0] and str(int(res)).rjust(sep_points + 1) or res == 0.5 and "=".rjust(
                    sep_points + 1) or (sep_points + 1) * " "
            else:
                tempo += res in [1, 0] and str(int(res)).rjust(sep_points) or res == 0.5 and "=".rjust(sep_points) or (
                    sep_points) * " "
        tempo += "  " + str(D[i][1]).rjust(ptsz) + "  "
            + str(D[i][2]).rjust(Sb) + ("\n" if i != len(D) - 1 else "")
        if not C:
            string += (len(tempo) - 1) * "=" + "\n"
            C=1
    return string + tempo
