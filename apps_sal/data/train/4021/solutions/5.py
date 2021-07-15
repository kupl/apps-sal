def elections_winners(votes, k):
    limit = max(votes)
    return sum(1 for vote in votes if (vote + k) > limit) + (votes.count(limit) == 1) * (k == 0)

