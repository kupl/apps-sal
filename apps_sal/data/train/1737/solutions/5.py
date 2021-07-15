def runoff(votes):
    voters, candidates = len(votes), votes[0]
    while votes:
        round = [vote[0] for vote in votes]
        polls = sorted((round.count(candidate), candidate) for candidate in candidates)
        min_poll, (max_poll, winner) = polls[0][0], polls[-1]
        if max_poll / voters > 0.5:
            return winner
        if len(polls) > 1 and max_poll == min_poll:
            return None
        loosers = [candidate for poll, candidate in polls if poll == min_poll]
        for voter in votes:
            for candidate in loosers:
                voter.remove(candidate)

