def disjunction(operands, is_exclusive):
    return sum(operands) & 1 if is_exclusive else any(operands)
