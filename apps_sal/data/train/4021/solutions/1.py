def elections_winners(votes, k):
    best = max(votes)
    if k == 0 and votes.count(best) == 1:
        return 1
    return len([x for x in votes if x + k > best])
