t = int(input())
for j in range(t):
    n = int(input())
    s = input()
    count1 = 0
    count2 = 0
    for i in range(len(s)):
        if s[i] == '1':
            count1 += 1
    for i in range(len(s)):
        if s[i] == '0':
            count2 += 1
    print(count1 * count2)
