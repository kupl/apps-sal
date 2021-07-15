
import collections


def convertInputToBrackets(arr):
    res = []

    for elem in arr:
        if elem == "1":
            res.append("(")
        elif elem == "2":
            res.append(")")
        elif elem == "3":
            res.append("[")
        elif elem == "4":
            res.append("]")

    return res


def solve(n, arr):
    balParanthesis, balBrackets = 0, 0
    balParans, balBracks = [0], [0]
    stack = []

    altDepth, maxAltDepth = 0, 0
    maxParanLength, maxBrackLength = 0, 0

    for ch in arr:
        if ch == ")" or ch == "]":
            if ch == ")":
                balParanthesis -= 1
            elif ch == "]":
                balBrackets -= 1

            lastCh, lastAltDepth = stack.pop()
            maxAltDepth = max(maxAltDepth, lastAltDepth)
        else:
            if ch == "(":
                balParanthesis += 1
            elif ch == "[":
                balBrackets += 1

            if not stack:
                stack.append((ch, 1))
            elif stack[-1][0] != ch:
                stack.append((ch, stack[-1][1] + 1))
            else:
                stack.append(stack[-1])

        balBracks.append(balBrackets)
        balParans.append(balParanthesis)

    lastParan, lastBrack = -1, -1

    for i in range(n+1):
        if balBracks[i] == 0:
            maxBrackLength = max(maxBrackLength, i-lastBrack)
            lastBrack = i

        if balParans[i] == 0:
            maxParanLength = max(maxParanLength, i - lastParan)
            lastParan = i

    return " ".join(map(str, (maxAltDepth, maxParanLength, maxBrackLength)))


n = int(input().strip())
arr = input().strip().split()
arr = convertInputToBrackets(arr)

print(solve(n, arr))

