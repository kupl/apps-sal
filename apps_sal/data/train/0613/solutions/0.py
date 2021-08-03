def check(s):
    arr = [s[0]]
    l = len(s)
    f1 = 0
    for i in range(1, l):
        if arr == []:
            arr.append(s[i])
        elif arr[-1] != s[i]:
            arr.append(s[i])
        else:
            del arr[-1]
    if arr == []:
        return True
    else:
        return False


count = 0
for t in range(eval(input())):
    s = input().strip()
    if check(s):
        count += 1
print(count)
