from string import ascii_lowercase


def rank(st, we, n):
    if not st:
        return "No participants"
    if n > len(st.split(',')):
        return "Not enough participants"
    x = ascii_lowercase
    s = 0
    winning_num = []
    names = []
    group = sorted(list(zip(st.split(','), we)))
    for name, weight in group:
        names.append(name)
        for letter in name.lower():
            s += (x.index(letter)) + 1
        s += len(name)
        winning_num.append(s * weight)
        s = 0
    final = list(zip(winning_num, names))
    final.sort(reverse=True)
    z = []
    final_names = []
    for V, N in final:
        final_names.append(N)
        if V == final[n - 1][0]:
            z.append(N)
    z.sort()
    ind = []
    for p in z:
        ind.append(final_names.index(p))
    new_list = final_names[:min(ind)] + z + final_names[max(ind) + 1:]
    return new_list[n - 1]
