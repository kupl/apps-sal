def solve(s):
    while "()" in s:
        s = s.replace("()", "")
    count = 0
    while len(s) > 1:
        count += s.count("((")
        s = s.replace("((", "")
        count += s.count("))")
        s = s.replace("))", "")
        count += (s.count(")(") * 2)
        s = s.replace(")(", "")
    return count if len(s) == 0 else -1
