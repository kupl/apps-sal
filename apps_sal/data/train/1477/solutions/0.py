for _1 in range(int(input())):
    n = int(input())
    s = input().strip()
    answer = s
    for i in range(len(s)):
        c = s[i]
        string = s[:i] + s[i + 1:]
        for j in range(len(string) + 1):
            answer = min(answer, string[:j] + c + string[j:])
    print(answer)
