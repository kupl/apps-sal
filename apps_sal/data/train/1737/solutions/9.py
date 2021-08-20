def runoff(voters):
    candidate_votes = {candidate: 0 for candidate in voters[0]}
    for voter in voters:
        candidate_votes[voter[0]] += 1
    total_votes = sum(candidate_votes.values())
    for x in list(candidate_votes.keys()):
        if candidate_votes[x] > total_votes / 2:
            return x
    least = min(candidate_votes.values())
    losers = [x for x in list(candidate_votes.keys()) if candidate_votes[x] == least]
    if len(losers) == len(list(candidate_votes.keys())):
        return None
    for voter in voters:
        for loser in losers:
            voter.remove(loser)
    return runoff(voters)
