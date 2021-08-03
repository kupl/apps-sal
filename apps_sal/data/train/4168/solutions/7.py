def string_hash(s):
    return (sum([ord(i) for i in s]) | sum([ord(s[j + 1]) - ord(i) for j, i in enumerate(s[:-1])])) & ((~sum([ord(i) for i in s])) << 2) ^ (32 * (s.count(" ") + 1))
