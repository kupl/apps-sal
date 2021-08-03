def addsup(a1, a2, a3):
    results = []
    for ele1 in a1:
        for ele2 in a2:
            if ele1 + ele2 in a3:
                results.append([ele1, ele2, ele1 + ele2])
    return results
