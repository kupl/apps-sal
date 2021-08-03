def solve(s):
    end = ""
    for i in range(1, len(s)):
        if s[i - 1].isdigit():
            end += s[i - 1]
            if s[i].isalpha():
                end += ","
        if i == len(s) - 1 and s[i].isdigit():
            end += s[i]
    return max(sorted([int(i) for i in end.split(",") if i != ""]))
