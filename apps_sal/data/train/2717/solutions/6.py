def scf(arr):
    div, all_div, diz = [], [], {}
    for x in arr:
        for i in range(2, x + 1):
            if not x % i:
                div.append(i)
        diz[x] = div
        all_div.extend(div)
        div = []
    all_div = sorted(set(all_div))
    return next((x for x in all_div if all(x in diz[it] for it in diz)), 1)
