abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
m = int(input())
string = input()
good = False
toCheck = []
lenS = len(string)
holes = [(-1, lenS)]
have = {'s': 0, 'i': 0, 'y': 0, 'h': 0, 'r': 0, 'f': 0, 'd': 0, 'z': 0, 'q': 0, 't': 0, 'n': 0, 'g': 0, 'l': 0, 'k': 0, 'o': 0, 'c': 0, 'w': 0, 'm': 0, 'b': 0, 'u': 0, 'a': 0, 'v': 0, 'e': 0, 'p': 0, 'j': 0, 'x': 0}
for sym in range(26):
    if not good:
        good = True
        for hole in holes:
            i = hole[0] + 1
            end = hole[1]
            while i < end:
                fill = string[i:min(end, i + m)].rfind(abc[sym])
                if fill == -1:
                    good = False
                    break
                else:
                    have[abc[sym]] += 1
                    i = i + fill + 1
                    if end - i < m:
                        break
            if not good:
                break
        holes = []
    if not good:
        have = {'s': 0, 'i': 0, 'y': 0, 'h': 0, 'r': 0, 'f': 0, 'd': 0, 'z': 0, 'q': 0, 't': 0, 'n': 0, 'g': 0, 'l': 0, 'k': 0, 'o': 0, 'c': 0, 'w': 0, 'm': 0, 'b': 0, 'u': 0, 'a': 0, 'v': 0, 'e': 0, 'p': 0, 'j': 0, 'x': 0}
        toCheck.append(abc[sym])
        good = True
        lastSeen = -1
        for i in range(lenS):
            if string[i] in toCheck:
                have[string[i]] += 1
                if i - lastSeen > m:
                    holes.append((lastSeen, i))
                    good = False
                lastSeen = i
        if lenS - lastSeen > m:
            holes.append((lastSeen, lenS))
            good = False
almost = [have[i] * i for i in abc]
print(''.join(almost))
