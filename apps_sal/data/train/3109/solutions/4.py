import re
def scramble_words(s):
    li = []
    for k in s.split():
        sp_chars = [[i, j] for j, i in enumerate(k) if not i.isalpha()]
        s = re.sub(r"[-,.']", "", k)
        result = [s[0]] + sorted(s[1:-1]) + [s[-1]]
        for i, j in sp_chars : result.insert(j, i)
        li.append(["".join(result),k][len(k)<4])
    return " ".join(li)
