def triangle(row):
    if len(row) == 1:
        return row[0]
    else:
        for v in range(0, len(row)):
            if v == 0:
                l = row
            else:
                l = lp
            lp = []
            for u in range(0, len(l) - 1):
                ft = l[u]
                st = l[u + 1]
                if ft == st:
                    lp.append(ft)
                elif ft == 'R' and st == 'G' or (ft == 'G' and st == 'R'):
                    lp.append('B')
                elif ft == 'R' and st == 'B' or (ft == 'B' and st == 'R'):
                    lp.append('G')
                elif ft == 'B' and st == 'G' or (ft == 'G' and st == 'B'):
                    lp.append('R')
        return l[len(l) - 1]
