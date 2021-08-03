def convertToParitys(s):
    """
    This converts the string s to an int, which is a bitMap of the parity of each letter
    odd ? = first bit set
    odd a = second bit set
    odd b = third bit set 
    etc
    """
    keys = '?abcdefghijklmnopqrstuvwxyz'
    paritys = {c: 0 for c in keys}
    for c in s:
        paritys[c] += 1
    for c, v in paritys.items():
        paritys[c] = v % 2

    out = 0
    bitValue = 1
    for c in keys:
        if paritys[c]:
            out += bitValue
        bitValue *= 2
    return out


def getSolutionBitMaps(s):
    """
    these are the 27 valid bitmaps that a substring can have
    even ? and the parities the same
    26 cases of odd ? and one bit different in the parity compared to s
    """
    out = []
    sP = convertToParitys(s)
    if sP % 2:
        sP -= 1  # to remove the '?' parity
    # even case -
    out.append(sP)
    # odd cases - need to xor sP with 1 + 2**n n = 1 to 26 inc to flip ? bit and each of the others
    for n in range(1, 27):
        out.append(sP ^ (1 + 2**n))
    return out


def getLeadingSubStringBitMapCounts(s):
    """
    This calculates the bit map of each of the len(s) substrings starting with the first character and stores as a dictionary.
    Getting TLE calculating each individually, so calculating with a single pass
    """
    out = {}
    bM = 0
    keys = '?abcdefghijklmnopqrstuvwxyz'
    paritys = {c: 0 for c in keys}
    values = {c: 2**i for i, c in enumerate(keys)}
    out[bM] = out.setdefault(bM, 0) + 1  # add the null substring
    bMis = []
    i = 0
    bMis = [0]
    for c in s:
        i += 1
        if paritys[c]:
            paritys[c] = 0
            bM -= values[c]
        else:
            paritys[c] = 1
            bM += values[c]
        out[bM] = out.setdefault(bM, 0) + 1
        bMis.append(bM)
    return out, bMis


def solve(s):
    out = 0
    bMjCounts, bMis = getLeadingSubStringBitMapCounts(s)
    # print('bMjCounts')
    # print(bMjCounts)
    solutions = getSolutionBitMaps(s)
    # print('solutions')
    # print(solutions)
    for bMi in bMis:
        for bMs in solutions:
            if bMs ^ bMi in bMjCounts:
                out += bMjCounts[bMs ^ bMi]
                # print(i,bMi,bMs,bMs^bMi,bMjCounts[bMs^bMi])
    if 0 in solutions:
        out -= len(s)  # remove all null substrings
    out //= 2  # since j may be less that i each substring is counted twice
    return out


T = int(input())
for tc in range(T):
    s = input()
    print(solve(s))
