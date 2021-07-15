def moves(st, ending):
    s = list(st)
    
    steps = 0
    for i in range(-1, -len(ending) - 1, -1):
        char = ending[i]
        while s[i] != char:
            # Find latest example of the missing char in the string prior to our position
            actual = [j for j, c in enumerate(s[:i]) if c == char][-1]
            # Transpose it with the character to its right
            s[actual], s[actual + 1] = s[actual + 1], s[actual]
            steps += 1

    while s[0] == '0':
        # Transpose first non-zero character with character to its left  
        actual = [j for j, c in enumerate(s) if c != '0'][0]
        s[actual - 1], s[actual] = s[actual], s[actual - 1]
        steps += 1
        
    return steps



def solve(n):
    print(f'n: {n}')
    s = str(n)
    _0, _2, _5, _7 = s.count('0'), s.count('2'), s.count('5'), s.count('7')
    
    best = not_possible = len(s) * 2 + 1
    if _0 > 1:
        # Enough 0s to end in ..00
        best = min(best, moves(s, '00'))
    if _2 and _5:
        # 2 & 5 present so we can end in ..25
        best = min(best, moves(s, '25'))
    if _5 and _0:        
        # 5 & 0 present so we can end in ..50
        best = min(best, moves(s, '50'))
    if _7 and _5:        
        # 7 & 5 present so we can end in ..75
        best = min(best, moves(s, '75'))

    if best == not_possible:
        best = -1
    return best

