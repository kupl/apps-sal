def elections_winners(votes, k):
  # coding and coding..
    win = max(votes)
    return sum(i + k > win for i in votes) or votes.count(win) == 1
