def solve(s):
    max_so_far = 0
    max_ending_here = 0
    for char in s:
        if isConsonant(char):
            max_ending_here += getValue(char)
            max_so_far = max(max_so_far, max_ending_here)
        else:
            max_ending_here = 0
    return max_so_far


def isConsonant(char):
    return char not in 'aeiou'


def getValue(char):
    return ord(char) & -ord('a')
