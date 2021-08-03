import sys


def run_length_compress(string):
    string = string + "@"
    n = len(string)
    begin = 0
    end = 1
    cnt = 1
    ans = []
    while True:
        if end >= n:
            break
        if string[begin] == string[end]:
            end += 1
            cnt += 1
        else:
            ans.append((cnt, string[begin]))
            begin = end
            end = begin + 1
            cnt = 1

    return ans


input = sys.stdin.readline


t = int(input())
for i in range(t):
    s = input()
    s = run_length_compress(s[0:-1])
    ans = 1
    for num, char in s:
        if char == "L":
            ans = max(num + 1, ans)
    print(ans)
