def scramble(s1, s2):
    def is_subsequence(needle, haystack):
        it = iter(haystack)
        return all(c in it for c in needle)
    return is_subsequence(sorted(s2), sorted(s1))
