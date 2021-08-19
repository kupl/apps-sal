t = int(input())
for i in range(t):
    s = input()
    l = [0 for i in range(26)]
    for j in range(len(s)):
        l[ord(s[j]) - 97] += 1
    f = 0
    for j in range(26):
        if l[j] > 1:
            f = 1
            break
    if f == 1:
        print('yes')
    else:
        print('no')
