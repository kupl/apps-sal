def transpose(amount, tab):
    col_tab = list(map(list, zip(*tab)))

    for i, j in enumerate(col_tab):
        double = False
        for a in range(len(j)):
            if col_tab[i][a].isdigit() and col_tab[i+1][a].isdigit():
                double = True
                col_tab[i][a] = col_tab[i][a] + col_tab[i+1][a]

        if double:
            col_tab.remove(col_tab[i+1])

    for i, j in enumerate(col_tab):
        for a in range(len(j)):
            if j[a].isdigit(): 
                new_note = int(j[a]) + amount
                if new_note < 0 or new_note > 22:
                    return 'Out of frets!'
                else:
                    col_tab[i][a]  = str(new_note)

    for j, k in enumerate(col_tab):
        if any(len(x) > 1 for x in k):
            col_tab[j] = [i + '-' if len(i) < 2 else i for i in k]
            
    return [''.join(j) for i, j in enumerate(list(map(list, zip(*col_tab))))]
