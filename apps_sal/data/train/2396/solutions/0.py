
def solve(s, c):
    if(len(s) == 1):
        if s[0] == c:
            return 0
        else:
            return 1
    ans1 = sum([i != c for i in s[:len(s) // 2]]) + solve(s[len(s) // 2:], chr(ord(c) + 1))
    ans2 = sum([i != c for i in s[len(s) // 2:]]) + solve(s[:len(s) // 2], chr(ord(c) + 1))
    return min(ans1, ans2)


for _ in range(int(input())):
    input()
    print(solve(input(), 'a'))
