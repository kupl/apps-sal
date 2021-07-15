def elections_winners(votes, k):
    max_so_far = max(votes)
    lst = [vote for vote in votes if vote + k > max_so_far]
    return len(lst) if lst else bool(votes.count(max_so_far) == 1)
