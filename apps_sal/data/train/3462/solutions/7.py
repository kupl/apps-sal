def disjunction(operands, is_exclusive):
    return sum(operands) % 2 if is_exclusive else any(operands)
