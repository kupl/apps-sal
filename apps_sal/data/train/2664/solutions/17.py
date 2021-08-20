def solve(s):
    reversed = s[::-1]
    middle = len(s) // 2
    count = 0
    for i in range(middle):
        if s[i] != reversed[i]:
            count += 1
    if middle * 2 == len(s):
        if count == 1:
            return True
    elif count == 0 or count == 1:
        return True
    return False
