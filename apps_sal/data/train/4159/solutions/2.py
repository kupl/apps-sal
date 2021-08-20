def poly_multiply(p1, p2):
    (r, s) = ({}, [])
    for i in range(len(p1)):
        for j in range(len(p2)):
            r[i + j] = r[i + j] + p1[i] * p2[j] if i + j in r else p1[i] * p2[j]
    for i in r:
        s.append(r[i])
    return s
