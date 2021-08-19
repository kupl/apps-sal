def elections_winners(votes, k):
    win = max(votes)
    return sum((i + k > win for i in votes)) or votes.count(win) == 1
