def create_report(a):
    d = {}
    for i in a:
        unique = [j for j in i.replace("-", " ").split(" ")[:-1] if j]
        curr = ["".join(unique).upper()[:6], "".join([k[:3] for k in unique]).upper(), "".join([k[:2] for k in unique]).upper(), "".join([j[:1] if k in [0, 1] else j[:2] for k, j in enumerate(unique)]).upper()][len(unique) - 1]
        d[curr] = d.get(curr, 0) + int(i.split(" ")[-1])
    return ["Disqualified data"] if "Labrador Duck" in "".join(a) else sum([[i, d[i]] for i in sorted(d)], [])
