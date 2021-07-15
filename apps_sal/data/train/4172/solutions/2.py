def solve(s):
    if len(s) % 2: return -1
    #imagine a simple symmetric random walk; '(' is a step up and ')' is a step down. We must stay above the original position
    height = 0; counter = 0
    for x in s:
        if x == '(':
            height += 1
        else:
            height -= 1
        if height < 0: 
            counter += 1
            height += 2
    #counter is the number of flips from ')' to '(', height//2 number of opposite flips
    return counter + height // 2
