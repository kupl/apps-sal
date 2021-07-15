def runoff(voters):
    if len(voters[0]) < 1:
        return None
    votes = count_votes(voters)
    possible_winner = get_winner(votes)
    if votes[possible_winner] > (len(voters) / 2):
        return possible_winner
    else:
        losers = get_losers(votes)
        new_voters = [[candidate for candidate in voter if candidate not in losers] for voter in voters]
        return runoff(new_voters)

def count_votes(voters):
    votes = {candidate: 0 for candidate in voters[0]}
    for voter in voters:
        votes[voter[0]] += 1
    return votes

def get_winner(votes):
    return max(votes, key=lambda x: votes[x])

def get_losers(votes):
    min_vote = min(votes.values())
    return [candidate for candidate in votes if votes[candidate] == min_vote]
