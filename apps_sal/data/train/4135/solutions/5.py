def solve(s):
    s = list(s)
    for i in range(len(s)):
        temp = s.copy()
        temp.pop(i)
        if all(temp.count(k) == temp.count(temp[0]) for k in temp) : return True
    return False
