def compute(s, c):
    bcount = s.count('B')
    gcount = s.count('G')
    if(abs(bcount - gcount) > 1):
        return -1
    stack = [(0, s[0])]
    bans = 0
    gans = 0
    for i in range(1, len(s)):
        if(len(stack) > 0 and stack[len(stack) - 1][1] != s[i]):
            idx, char = stack[len(stack) - 1]
            if((idx % 2 and s[i] == 'B') or (i % 2 and char == 'B')):
                bans += abs(i - idx)**c
            elif((idx % 2 and s[i] == 'G') or (i % 2 and char == 'G')):
                gans += abs(i - idx)**c
            stack.pop(len(stack) - 1)
        else:
            stack.append((i, s[i]))

    if(gcount == bcount):
        return min(bans, gans)
    elif(gcount > bcount):
        return bans
    return gans


for t in range(int(input())):
    c = int(input())
    print(compute(input(), c))
