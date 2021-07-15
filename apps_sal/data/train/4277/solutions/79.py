def difference_in_ages(age):
    ergebnis = []
    ergebnis.append(sorted(age)[0])
    ergebnis.append(sorted(age)[-1])
    ergebnis.append(ergebnis[-1]-ergebnis[0])
    return tuple(ergebnis)
