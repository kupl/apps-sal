for i in range(int(input())):
    n = int(input())
    s = [x for x in input().strip()]
    cnt = 0
    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1]:
            cnt += 1
    print(cnt)
