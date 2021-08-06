t = int(input())
ans = []
while t > 0:
    dic_a = {}
    dic_b = {}
    a = input()
    b = input()
    common = 0
    for letter in a:
        if letter in dic_a:
            dic_a[letter] += 1
        else:
            dic_a[letter] = 1
    for letter in b:
        if letter in dic_b:
            dic_b[letter] += 1
        else:
            dic_b[letter] = 1
    if len(a) > len(b):
        for key in dic_a:
            if key in dic_b:
                common += min(dic_a[key], dic_b[key])
    else:
        for key in dic_b:
            if key in dic_a:
                common += min(dic_a[key], dic_b[key])
    ans.append(common)
    t -= 1
for an in ans:
    print(an)
