try:
    t = int(input())
    for i in range(t):
        (n, k) = map(int, input().split())
        s = input()
        l = [-1] * len(s)
        numb = s.count('b')
        x = numb
        for j in range(len(s)):
            if s[j] == 'a':
                l[j] = numb
            if s[j] == 'b':
                numb = numb - 1
        count1 = 0
        for j in range(len(l)):
            if l[j] > 0:
                count1 = count1 + k * (2 * l[j] + (k - 1) * x) // 2
            elif l[j] == 0:
                count1 = count1 + k * (2 * 0 + (k - 1) * x) // 2
        print(count1)
except:
    pass
