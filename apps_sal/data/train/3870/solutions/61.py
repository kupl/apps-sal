def solve(s):
    space = []
    count = 0
    res = ""
    for c in s:
        count += 1
        if c.isalnum() == True:
            res = c + res
        elif c == " ":
            space.append(count)
    for num in space:
        res = res[:num-1] + " " + res[num-1:]
    return res

