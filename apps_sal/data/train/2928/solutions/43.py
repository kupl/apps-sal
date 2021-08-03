def alphabet_war(fight):
    leftDict = {"w": 4, "p": 3, "b": 2, "s": 1}
    rightDict = {"m": 4, "q": 3, "d": 2, "z": 1}
    totalSum = sum(leftDict[x] if x in leftDict else -rightDict[x] if x in rightDict else 0 for x in fight)
    return "Let's fight again!" if totalSum == 0 else "Left side wins!" if totalSum > 0 else "Right side wins!"
