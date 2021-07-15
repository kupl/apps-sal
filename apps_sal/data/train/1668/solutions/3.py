from operator import itemgetter

def next_smaller(n):
    s        = str(n)
    LR_Pairs = list(enumerate(zip(s,s[1:])))                                                    # Association pair (l,r) and index of left char of the pair
    iP,pivot = next( ((i,l) for i,(l,r) in reversed(LR_Pairs) if l>r), (-1,-1) )                # Extract first increasing pair, coming from the end,...
                                                                                                # ... then get the left char (pivot) and it's index
    if iP == -1: return -1                                                                      # No smaller number...
    
    iM,mx = max( ((i,c) for i,c in enumerate(s[iP+1:],iP+1) if c < pivot), key=itemgetter(1))   # Highest char smaller than 'pivot' and its index
    nextS = s[:iP] + mx + ''.join(sorted(s[iP:iM]+s[iM+1:], reverse=True))                      # Move 'mx' in place of 'pivot', then sort all the remaining chars, descending
    
    return int(nextS) if nextS[0] != '0' else -1
