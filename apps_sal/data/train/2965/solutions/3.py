def solve_eq(eq):
    for i in range(3):
        if eq[i][i] == 0:
            (eq[i], eq[i + 1]) = (eq[i + 1], eq[i])
        eq[i] = [x / eq[i][i] for x in eq[i]]
        for j in range(3):
            if i != j:
                eq[j] = [-eq[j][i] * eq[i][x] + eq[j][x] for x in range(len(eq[j]))]
    return [round(x[-1]) for x in eq]
