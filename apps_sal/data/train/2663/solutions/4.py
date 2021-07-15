def addsup(a1, a2, a3):
    r = {}
    for s in a3:
      for i in a1:
          r[s-i] = [i] + r.get(s-i, [])
    result = []
    for j in a2:
        if j in r:
            for i in r[j]:
                result.append([i, j, j+i])
    return result
