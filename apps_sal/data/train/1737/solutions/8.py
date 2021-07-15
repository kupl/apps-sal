from collections import Counter

def runoff(voters):
    half_voters = len(voters)/2
    tally = {}
    for votes in voters:
        vote = votes[0]
        if vote in tally:
            tally[vote] += 1
        else:
            tally[vote] = 1
            
    high_counts = Counter(tally).most_common()
        
    if high_counts[0][1] > half_voters:
        return high_counts[0][0]
        
    
    lowest = []
    
    lowest_count = -1
    
    for i in range(len(high_counts)):
        current = high_counts[(-1 - i)]
        if current[1] == lowest_count or lowest_count == -1:
            lowest_count = current[1]
            lowest.append(current[0])
        else: break
    
    if len(lowest) == len(high_counts):
        return None
    
    voters = [[vote for vote in votes if (vote in tally) and (vote not in lowest)] for votes in voters]
    
    return runoff(voters)
