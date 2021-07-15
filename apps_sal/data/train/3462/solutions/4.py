from functools import reduce

def disjunction(operands, is_exclusive):
    return reduce(getattr(bool, f"__{'x' if is_exclusive else ''}or__"), operands)
