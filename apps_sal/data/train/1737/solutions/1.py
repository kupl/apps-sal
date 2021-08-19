from collections import Counter


def runoff(voters):
    numVoters = len(voters)
    while voters[0]:
        c = Counter((voters[i][0] for i in range(numVoters)))
        maxVote = max(c.values())
        if maxVote > numVoters / 2:
            return [elt for elt in c if c[elt] == maxVote][0]
        for k in set(c.keys()) ^ set(voters[0]):
            c[k] = 0
        minVote = min(c.values())
        voters = [[p for p in v if not p in [elt for elt in c if c[elt] == minVote]] for v in voters]
    return None
