def solve(s):
    return any((s[i + 1:] + s[:i + 1] == s[i::-1] + s[:i:-1] for i in range(len(s))))
