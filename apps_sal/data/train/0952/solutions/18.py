try:
    T = int(input())
    for i in range(T):
        s = input()
        w = [1, 5, 9, 15, 21]
        l = ["a", "e", "i", "0", "u"]
        cnt = 0
        for j in range(len(s)):
            if s[j] not in l:
                cnt = cnt + min(abs(ord(s[j]) - 96 - w[0]), abs(ord(s[j]) - 96 - w[1]), abs(ord(s[j]) - 96 - w[2]), abs(ord(s[j]) - 96 - w[3]), abs(ord(s[j]) - 96 - w[4]))
        print(cnt)
except:
    pass
