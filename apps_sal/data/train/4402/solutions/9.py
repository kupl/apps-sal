def solve(s):
    return "".join(sorted(list(s), key=str.lower)) in "abcdefghijklmnopqrstuvwxyz"
