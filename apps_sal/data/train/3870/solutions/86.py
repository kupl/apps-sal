def solve(s):
    revs = s[::-1]
    revs = "".join(revs.split())
    output = ""
    count = 0

    for letter in s:
        if letter != " ":
            output = output + revs[count]
            count += 1
        else:
            output = output + " "
    return output
