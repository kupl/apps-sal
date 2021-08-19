G = {0: [1, 4, 5], 1: [0, 2, 6], 2: [1, 3, 7], 3: [2, 4, 8], 4: [3, 0, 9], 5: [0, 7, 8], 6: [1, 8, 9], 7: [2, 5, 9], 8: [3, 5, 6], 9: [4, 6, 7]}
L = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'A', 6: 'B', 7: 'C', 8: 'D', 9: 'E'}


def Check(S):
    result = ''
    possibleStart = [k for k in list(L.keys()) if L[k] == S[0]]
    isBreak = False
    for c in S:
        found = False
        if result == '':
            result = result + str(possibleStart[0])
            last = possibleStart[0]
            found = True
        else:
            for k in G[last]:
                if L[k] == c:
                    result = result + str(k)
                    last = k
                    found = True
        if not found:
            isBreak = True
            break
        # print result
    if not isBreak:
        return result
    result = ''
    # print 'nextstart'
    for c in S:
        found = False
        if result == '':
            result = result + str(possibleStart[1])
            last = possibleStart[1]
            found = True
        else:
            for k in G[last]:
                if L[k] == c:
                    result = result + str(k)
                    last = k
                    found = True
        if not found:
            return str(-1)
        # print result
    return result


T = int(input())
while T > 0:
    T = T - 1
    S = input()
    R = Check(S)
    print(R)
