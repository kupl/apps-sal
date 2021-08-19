def solve(s):
    return max(map(int, ''.join((elem if elem.isdigit() else ' ' for elem in s)).split()))
