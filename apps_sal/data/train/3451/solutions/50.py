def triangle(row):
    act = row
    nex = ''
    while len(act) > 2:
        for i in range(len(act) - 1):
            if act[i] == act[i + 1]:
                nex = nex + act[i]
            elif act[i] == 'R' and act[i + 1] == 'G' or (act[i] == 'G' and act[i + 1] == 'R'):
                nex = nex + 'B'
            elif act[i] == 'B' and act[i + 1] == 'G' or (act[i] == 'G' and act[i + 1] == 'B'):
                nex = nex + 'R'
            elif act[i] == 'R' and act[i + 1] == 'B' or (act[i] == 'B' and act[i + 1] == 'R'):
                nex = nex + 'G'
        act = nex
        nex = ''
    if len(act) == 2:
        if act[0] == act[1]:
            return act[0]
        elif act[0] == 'R' and act[1] == 'G' or (act[0] == 'G' and act[1] == 'R'):
            return 'B'
        elif act[0] == 'B' and act[1] == 'G' or (act[0] == 'G' and act[1] == 'B'):
            return 'R'
        elif act[0] == 'R' and act[1] == 'B' or (act[0] == 'B' and act[1] == 'R'):
            return 'G'
    else:
        return act[0]
