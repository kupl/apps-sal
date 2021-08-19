def solve(n):
    sn = str(n)
    ret = 0
    if n % 25 == 0:
        return ret

    if not (sn.count('0') >= 2 or ('5' in sn and ('0' in sn or '2' in sn or '7' in sn))):
        return -1

    zeroes = []
    two = -1
    five = -1
    seven = -1
    for c in range(len(sn)):
        if sn[c] == '0':
            zeroes.append(c)
        elif sn[c] == '2':
            two = c
        elif sn[c] == '5':
            five = c
        elif sn[c] == '7':
            seven = c

    minlen = 2 * len(sn)
    if len(zeroes) > 1:
        # '00' possible
        # move last 0 to last place
        steps = len(sn) - zeroes[-1] - 1
        # move second to last 0 to last place but 1
        steps += len(sn) - zeroes[-2] - 2
        minlen = min(minlen, steps)

    if five != -1:
        # 25
        if two != -1:
            steps = 2 * len(sn) - five - two - 3
            if five < two:
                steps += 1
            # check for leading zeroes
            min25 = min(two, five)
            max25 = max(two, five)
            popsn = sn[:min25] + sn[min25 + 1:max25] + sn[max25 + 1:]
            update = False
            while len(popsn) > 0 and popsn[0] == '0':
                steps += 1
                update = True
                popsn = popsn[1:]
            minlen = min(minlen, steps)
        # 50
        if zeroes != []:
            steps = 2 * len(sn) - five - zeroes[-1] - 3
            if zeroes[-1] < five:
                steps += 1
            # check for leading zeroes
            min50 = min(zeroes[-1], five)
            max50 = max(zeroes[-1], five)
            popsn = sn[:min50] + sn[min50 + 1:max50] + sn[max50 + 1:]
            update = False
            while len(popsn) > 0 and popsn[0] == '0':
                steps += 1
                update = True
                popsn = popsn[1:]
            minlen = min(minlen, steps)
        # 75
        if seven != -1:
            steps = 2 * len(sn) - five - seven - 3
            if five < seven:
                steps += 1
            # check for leading zeroes
            min75 = min(five, seven)
            max75 = max(five, seven)
            popsn = sn[:min75] + sn[min75 + 1:max75] + sn[max75 + 1:]
            update = False
            while len(popsn) > 0 and popsn[0] == '0':
                steps += 1
                update = True
                popsn = popsn[1:]
            minlen = min(minlen, steps)
    return minlen
