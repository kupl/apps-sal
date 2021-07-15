import itertools

def transpose(amount, tab):
    shorten_dash = False
    for i in range(0,6):
        split_i = ["".join(y) for x,y in itertools.groupby(tab[i],key=str.isdigit)]
        trans = ""
        for gr in split_i:
            if gr.isnumeric():
                old = int(gr)
                new = old + amount
                if not 0 <= new <=22: return 'Out of frets!'
                trans += str(new)
                if (old < 10) and (new >= 10):
                    ins = len(trans) - 1
                    for j in range(0,6):
                        if not j == i:
                            if tab[j][ins-1:ins+1].isdigit(): shorten_dash = True
                    if not shorten_dash:
                        for j in range(0,6):
                            if not j == i:
                                tab[j] = tab[j][:ins] + "-" + tab[j][ins:]
                if (old >= 10) and (new < 10):
                    ins = len(trans)
                    add_dash = False
                    for j in range(0,6):
                        if not j == i:
                            if tab[j][ins-1:ins+1].isdigit(): add_dash = True
                    if add_dash:
                        trans += "-"
                    else:
                        for j in range(0,6):
                            if not j == i:
                                tab[j] = tab[j][:ins] + tab[j][ins+1:]
            else:
                if shorten_dash:
                    gr = gr[1:]
                    shorten_dash = False
                trans += gr
        tab[i] = trans
    return tab
