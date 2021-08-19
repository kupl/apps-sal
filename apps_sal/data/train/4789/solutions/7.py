from itertools import combinations


def sat(f: Formula) -> set or False:

    def eval_sat(f: Formula, true_vars: set) -> bool:
        if f.is_literal():
            return f in true_vars
        elif f.is_and():
            return all((eval_sat(ff, true_vars) for ff in f.args))
        elif f.is_or():
            return any((eval_sat(ff, true_vars) for ff in f.args))
        elif f.is_not():
            return not eval_sat(*f.args, true_vars)

    def get_vars(f: Formula) -> set:
        if f.is_literal():
            return {f}
        else:
            return set((var for ff in f.args for var in get_vars(ff)))
    variables = get_vars(f)
    for i in range(len(variables) + 1):
        for true_vars in map(set, combinations(variables, i)):
            if eval_sat(f, true_vars):
                return true_vars
    return False
