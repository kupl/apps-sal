def solve(s):
    if s == s[::-1] and len(s) % 2 == 0:
        return False

    start = 0
    end = len(s) - 1
    mid = end // 2
    count = 0
    while start < mid:
        for i in range(mid):
            if s[start] != s[end]:
                count += 1
            start += 1
            end -= 1
    if count <= 1:
        return True
    return False
