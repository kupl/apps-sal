s = input()
res = 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        for k in range(j + 1, len(s)):
            if s[i] + s[j] + s[k] == "QAQ":
                res += 1
print(res)
