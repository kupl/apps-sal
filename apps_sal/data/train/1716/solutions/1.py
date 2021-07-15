from functools import lru_cache as memo
from itertools import permutations, product
from operator import add, sub, mul, truediv as div
operators = {add: '+', sub: '-', mul: '*', div: '/'}

@memo(None)
def evaluate_tree(terms, ops):
    if not ops: return {terms[0]: str(terms[0])}
    results = {}
    for idx, op in enumerate(ops, 1):
        left, right = evaluate_tree(terms[:idx], ops[:idx-1]), evaluate_tree(terms[idx:], ops[idx:])
        results.update({op(l, r): f'({left[l]}){operators[op]}({right[r]})'
                        for l, r in product(left, right) if not (op == div and r == 0)})
    return results

def equal_to_24(*terms):
    for operands in permutations(terms):
        for ops in product(operators, repeat=3):
            results = evaluate_tree(operands, ops)
            if 24 in results: return results[24]
    return "It's not possible!"
