def solve(n):
    s = str(n)
    l = len(s)
    if l == 1 or (l == 2 and s[1] in {"8", "9"}):
        return n
    for i in range(l - 1):
        if s[i + 1] != "9":
            return int(f"{s[:i]}{int(s[i]) - 1}{'9' * (l - i - 1)}")
