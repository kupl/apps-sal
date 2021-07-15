def elections_winners(votes, k):
    m = max(votes)
    return [0, 1][votes.count(m) == 1] if not k else sum(i + k > m for i in votes) 
