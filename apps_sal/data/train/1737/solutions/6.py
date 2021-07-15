from collections import Counter

def runoff(voters):
    while sum(voters, []):
        poll = Counter(ballot[0] for ballot in voters)
        
        scores = sorted(poll.values())
        if scores[-1] * 2 > len(voters):
            return next((c for c in poll if poll[c] == scores[-1]))
        elif scores[-1] == scores[0]:
            return
        voters = [[c for c in voter if poll[c]  > scores[ 0]] for voter in voters]

