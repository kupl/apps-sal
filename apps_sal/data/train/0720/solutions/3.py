try:
    for i in range(int(input())):
        s = input()
        n = len(s)
        count = 0
        ones = [0] * (n + 1)
        for i in range(n):
            if s[i] == '1':
                ones[i + 1] = ones[i] + 1
            else:
                ones[i + 1] = ones[i]
        i = 1
        r = 2
        while r <= n:
            r = i + i * i
            j = 0
            while j <= n - r:
                if ones[j + r] - ones[j] == i:
                    count += 1
                    j += 1
                else:
                    j += abs(i - (ones[j + r] - ones[j]))
            i += 1
        print(count)
except:
    pass
