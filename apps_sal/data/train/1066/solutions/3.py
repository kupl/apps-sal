# cook your dish here
try:
    def increasing(n):
        if 0 <= n <= 9:
            return n

        def fi(s):
            for i in range(len(s) - 1):
                if s[i] > s[i + 1]:
                    return i
            return -1
        s = str(n)
        n = len(s)
        r = fi(s)
        l = s.index(s[r])
        if r == -1:
            return n
        else:
            return int(s[:l] + str(int(s[l]) - 1) + '9' * (n - l - 1))
    for _ in range(int(input())):
        n = int(input())
        ans = increasing(n)
        print(ans)
except EOFError as e:
    pass
