from collections import deque

def group_cities(seq):
    result = []
    
    # Remove duplicates
    seq = sorted(set(seq))

    # Convert to lower case for comparisons
    simples = [c.lower() for c in seq]
    
    # Indices that have already been added to a set
    skip = set()
    
    # Look for matches
    for i, c1 in enumerate(simples):
        if i in skip:
            # Already matched
            continue
        city_match = [i]
        skip.add(i)
        
        # Create all the rolled versionos of this city name
        rolls = []
        roller = deque(c1)
        roller.rotate(1)
        while ''.join(roller) != c1:
            rolls.append(''.join(roller))
            roller.rotate(1)
        
        # See if a rolled name is present in any names later in the list
        for roll in rolls:
            for j, c2 in enumerate(simples[i + 1:], i + 1):
                if j in skip:
                    # Already matched
                    continue
                if c2 == roll:
                    # Found a matching name, add this index to the matches and skip set
                    skip.add(j)
                    city_match.append(j)
        
        # Convert matched indices back to original name
        result.append(sorted([seq[k] for k in city_match]))
    
    # Sort by decreasing length and then alphabetically
    result.sort(key=lambda a: (-len(a), a[0]))
    return result

