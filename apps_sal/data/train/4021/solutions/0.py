def elections_winners(votes, k):
    m = max(votes)
    return sum((x + k > m for x in votes)) or votes.count(m) == 1
