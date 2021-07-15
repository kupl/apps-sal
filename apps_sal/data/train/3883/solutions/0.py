def solve(s):
    vowels = sorted(c for c in s if c in "aeiou")
    consonants = sorted(c for c in s if c not in "aeiou")
    part1, part2 = sorted((vowels, consonants), key=len, reverse=True)
    part2.append('')
    if len(part1) > len(part2):
        return "failed"
    return "".join(a + b for a, b in zip(part1, part2))
