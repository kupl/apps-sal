def solve(a, b):
    if not a:
        return 1
    if not b:
        return 0
    if b[0].lower() == a[0].lower():
        return solve(a, b[1:]) + solve(a[1:], b[1:])
    else:
        return solve(a, b[1:])
