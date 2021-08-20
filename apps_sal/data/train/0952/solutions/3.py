try:
    for _ in range(int(input())):
        s = input()
        cost = 0
        for i in range(len(s)):
            if s[i] not in 'aeiou':
                n = ord(s[i]) - 96
                cost += min(abs(n - 1), abs(n - 5), abs(n - 9), abs(n - 15), abs(n - 21))
        print(cost)
except:
    pass
