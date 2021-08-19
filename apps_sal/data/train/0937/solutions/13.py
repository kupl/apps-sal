def chefdailyRoutine(s):
    flag = 1
    for i in range(1, len(s)):
        if ord(s[i]) < ord(s[i - 1]):
            flag = 0
            break
    if flag == 1:
        print('yes')
    else:
        print('no')
    return


# Driver code starts here
t = int(input())
for _ in range(t):
    s = input()
    chefdailyRoutine(s)
