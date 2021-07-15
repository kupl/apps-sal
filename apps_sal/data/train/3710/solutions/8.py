import time
from heapq import heappush, heappop, heapify
 

def ulam_sequence(u, v, numTerms):
    
    terms = [u, v] # This is the sequence we are producing.
    sumsDict = dict([(u, 1), (v,1), (u+v, 1)]) # This is a dict of sums so far.  So e.g. 5:2 means there are 2 ways to get 2 terms in the sequence to add to 5.
    sumsHeap = [u, v, u+v] # Sorted list of those sums.
    heapify(sumsHeap) 
    deletedDict = dict() # This is a list of sums that have already reached a value of 2 or more.  No point looking at these again.

    # The idea is to go through the sorted list of sums (previous terms in sequence added together)
    # and find the minimum of those and add that to the sequence.
    while True:
        
        while True:
            numtoBeAppended = heappop(sumsHeap)
            if numtoBeAppended > terms[-1] and numtoBeAppended in sumsDict:
                break
            
            
        terms.append(numtoBeAppended)
        if len(terms) >= numTerms:
            break
        
        for term in terms[:-1]:
            entry = term + numtoBeAppended
            if entry in sumsDict:
                # If it's already in the heap then there are more than one ways to sum to 
                # this value, so remove it, it will never be part of the sequence
                del sumsDict[entry]
                deletedDict[entry] = True
            else:
                # If we haven't already marked it as being seen before (and so, deleted) add it to our heap
                if entry not in deletedDict:
                    heappush(sumsHeap, entry)
                    sumsDict[entry] =    1
            
                

    return terms
