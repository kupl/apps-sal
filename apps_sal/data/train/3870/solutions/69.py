def solve(s):
    x = s.split(" ")

    r = []
    for i in x:
        rt = [""] * len(i)
        r.extend(rt)
        r.extend([" "])

    r = r[:len(r) - 1]

    counter = 0
    for i in reversed(x):
        for j in reversed(i):
            if r[counter] == "":
                r[counter] = j
            else:
                r[counter + 1] = j
                counter += 1
            counter += 1

    return "".join(r)
