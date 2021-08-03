for t in range(int(input())):
    n = int(input())
    s = input()
    count1 = count2 = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] != '1':
                count1 += 1
            if s[i] != '0':
                count2 += 1
        if i % 2 == 1:
            if s[i] != '0':
                count1 += 1
            if s[i] != '1':
                count2 += 1
    print(min(count1, count2))
