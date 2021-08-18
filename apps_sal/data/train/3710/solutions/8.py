import time
from heapq import heappush, heappop, heapify


def ulam_sequence(u, v, numTerms):

    terms = [u, v]
    sumsDict = dict([(u, 1), (v, 1), (u + v, 1)])
    sumsHeap = [u, v, u + v]
    heapify(sumsHeap)
    deletedDict = dict()

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
                del sumsDict[entry]
                deletedDict[entry] = True
            else:
                if entry not in deletedDict:
                    heappush(sumsHeap, entry)
                    sumsDict[entry] = 1

    return terms
