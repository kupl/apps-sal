T = int(input())
for i in range(T):
    s = input()
    count = 0
    for j in range(1, len(s)):
        if s[j] == "C" and s[j - 1] == 'C':
            count += 1
        elif s[j] == 'E':
            if s[j - 1] == 'C' or s[j - 1] == 'E':
                count += 1
        elif s[j] == 'S':
            if s[j - 1] == 'E' or s[j - 1] == 'C' or s[j - 1] == 'S':
                count += 1
    if count == len(s) - 1:
        print("yes")
    else:
        print('no')
