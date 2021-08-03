def combos(n):
    combinatorialations, answer, seen = map(lambda x: [x], list(range(1, n + 1))), [], set()
    while len(combinatorialations):
        acombo = combinatorialations.pop()
        thesum = sum(acombo)
        if thesum == n:
            answer.append(acombo)
            continue
        for i in range(1, n):
            if i + thesum > n:
                break
            newcombo = sorted(acombo + [i])
            tup = tuple(newcombo)
            if tup in seen:
                continue
            seen.add(tup)
            combinatorialations.append(newcombo)
    return answer
