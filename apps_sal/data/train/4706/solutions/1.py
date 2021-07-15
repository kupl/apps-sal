def split_exp(n):
    j = n.find('.') + 1 or len(n) + 1
    return [f"{c}{'0'*(j-i-2)}" if i < j else f".{'0'*(i-j)}{c}" for i,c in enumerate(n) if c not in "0."]
