from itertools import count

# Couldn't find the pattern of why it's 1 or 8, I'm sad :(
def repeat_sequence_len(n):
    memo = {}
    for i in count():
        if n in memo: return i - memo[n]
        memo[n] = i
        n = sum(d*d for d in map(int, str(n)))
