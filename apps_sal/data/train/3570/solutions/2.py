def solve(r):
    ǂ = 1
    for x in sorted(r):
        if x > ǂ:
            break
        else: ǂ += x
    return ǂ
