from collections import Counter


def runoff(voters):
    while voters[0]:
        poll = Counter((ballot[0] for ballot in voters))
        (winner, maxscore) = max(poll.items(), key=lambda x: x[1])
        minscore = min(poll.values())
        if maxscore * 2 > len(voters):
            return winner
        voters = [[c for c in voter if poll[c] > minscore] for voter in voters]
