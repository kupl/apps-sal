

import string
punc = [".", "'", ",", ":", ";"]
res = []
for _ in range(int(input())):
    s = input()
    for i in s:
        if i in punc:
            s = s.replace(i, "")
    s = s.split()
    res.append(s)
for i in range(len(res) - 1, -1, -1):
    print(" ".join(res[i][::-1]))
