def group_check(s):
    while "()" in s or "{}" in s or "[]" in s:
        s = s.replace("()", "")
        s = s.replace("{}", "")
        s = s.replace("[]", "")
    return len(s) == 0
