def solve(s):
    return max(map(int, "".join(" " if x.isalpha() else x for x in s).split()))
