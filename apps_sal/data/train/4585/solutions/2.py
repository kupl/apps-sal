# Precompute all 2 digit suffixes into an associated prefix and repeating loop
# E.g. build until we get two repeating values:
#   98 -> [17, 8, 15, 6, 11, 2, 3, 5, 8, 13, 4, 7, 11, 2] (Note: [11, 2] is repeated)
#   -> Prefix '17815611', Loop: '2358134711'
#
# Now any number ending with 98 has a predefined prefix and cycle, e.g.:
#   123 + 598 -> 123598 -> 98 -> Prefix '17815611', Loop: '2358134711'
# Hence 123 + 598 starts with '12359817815611' and then repeats '2358134711' indefinitely

# Dict[str, Tuple[str, str]]
lookup = {}
for i in range(10):
    for j in range(10):
        start = f'{i}{j}'
        n = int(start)
        s = [0, n]
        seen = {}
        while True:
            x = s[-1]
            if x < 10:
                x = x + s[-2] % 10
            else:
                x = (x // 10) + (x % 10)
            
            pair = (s[-1], x)
            if pair not in seen:
                s.append(x)
                seen[pair] = len(s)
            else:
                # idx is the point where prefix finishes and loop starts
                idx = seen[pair] - 1
                prefix = s[2:idx]  # Skip the leading zero and the starting value
                loop = s[idx:]
                lookup[start] = (''.join(map(str, prefix)), ''.join(map(str, loop)))
                break

def find(a, b, n):
    start = f'{a}{b}'[-2:].rjust(2, '0')
    prefix, loop = lookup[start]
    s = str(a) + str(b) + prefix + loop
    
    if n < len(s):
        # Digit in initial supplied digits, the sum of their last two digits or the prefix
        return int(s[n])

    # Digit is in the loop
    m = (n - len(s)) % len(loop)
    return int(loop[m])

